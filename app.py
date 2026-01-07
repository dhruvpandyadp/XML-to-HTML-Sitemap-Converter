import streamlit as st
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from collections import defaultdict
import time

st.set_page_config(page_title="XML to HTML Sitemap Converter", page_icon="🗺️", layout="wide")

# Custom CSS for better styling with light/dark mode support
st.markdown("""
<style>

 .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

 /* Footer styling for light/dark mode */
    .footer-container {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    .footer-container p {
        margin: 0px 0px 0rem;
    }

</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("""
<div class="main-header">
    <h1>🗺️ XML to HTML Sitemap Converter</h1>
    <p><strong>Convert your XML sitemaps into organized HTML sitemaps</strong></p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'sitemap_data' not in st.session_state:
    st.session_state.sitemap_data = None
if 'categories' not in st.session_state:
    st.session_state.categories = []
if 'discovered_sitemaps' not in st.session_state:
    st.session_state.discovered_sitemaps = {}
if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = []

def fetch_page_title(url, timeout=5):
    """Fetch the title of a webpage"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title')
        return title.string.strip() if title else url
    except Exception as e:
        return url

def parse_xml_sitemap(sitemap_url):
    """Parse XML sitemap and extract URLs"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(sitemap_url, headers=headers, timeout=10)
        response.raise_for_status()

        root = ET.fromstring(response.content)

        # Handle namespace
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        urls = []
        # Check if it's a sitemap index
        sitemap_elements = root.findall('.//ns:sitemap/ns:loc', namespace)
        if sitemap_elements:
            # It's a sitemap index, return child sitemaps
            return [elem.text for elem in sitemap_elements], True
        else:
            # It's a regular sitemap, extract URLs
            url_elements = root.findall('.//ns:url/ns:loc', namespace)
            return [elem.text for elem in url_elements], False

    except Exception as e:
        st.error(f"Error parsing {sitemap_url}: {str(e)}")
        return [], False

def categorize_sitemap(sitemap_url):
    """Categorize sitemap based on filename"""
    filename = sitemap_url.split('/')[-1].lower()

    # Remove numbers and .xml extension for categorization
    base_name = re.sub(r'\d+', '', filename).replace('.xml', '').replace('-', ' ').strip()

    if 'post' in base_name and 'sitemap' in base_name:
        return 'Post Sitemap'
    elif 'page' in base_name and 'sitemap' in base_name:
        return 'Page Sitemap'
    elif 'category' in base_name:
        return 'Category Sitemap'
    elif 'tag' in base_name:
        return 'Tag Sitemap'
    elif 'author' in base_name:
        return 'Author Sitemap'
    elif 'product' in base_name:
        return 'Product Sitemap'
    else:
        return 'Other Sitemap'

def discover_sitemaps(sitemap_urls):
    """Discover all sitemaps and categorize them without crawling URLs"""
    discovered = defaultdict(lambda: {'sitemaps': [], 'url_count': 0})

    status_text = st.empty()
    progress_bar = st.progress(0)
    current_check = st.empty()

    all_sitemaps = []

    # Step 1: Collect all sitemap URLs
    status_text.markdown("### 🔍 Discovering sitemaps...")
    for idx, url in enumerate(sitemap_urls):
        current_check.info(f"📄 Checking: `{url}`")
        urls, is_index = parse_xml_sitemap(url)
        if is_index:
            all_sitemaps.extend(urls)
            current_check.success(f"✅ Found {len(urls)} sub-sitemaps in index")
        else:
            all_sitemaps.append(url)
            current_check.success(f"✅ Regular sitemap detected")
        time.sleep(0.2)

    # Step 2: Categorize and count URLs
    status_text.markdown(f"### 📊 Analyzing {len(all_sitemaps)} sitemap(s)...")

    for idx, sitemap_url in enumerate(all_sitemaps):
        sitemap_name = sitemap_url.split('/')[-1]
        current_check.info(f"🔄 Analyzing: `{sitemap_name}`")

        urls, is_index = parse_xml_sitemap(sitemap_url)
        if not is_index and urls:
            category = categorize_sitemap(sitemap_url)
            discovered[category]['sitemaps'].append(sitemap_url)
            discovered[category]['url_count'] += len(urls)

            current_check.success(f"✅ `{sitemap_name}` → **{category}** ({len(urls)} URLs)")

        progress_bar.progress((idx + 1) / len(all_sitemaps))
        time.sleep(0.2)

    status_text.markdown("### ✅ Discovery Complete!")
    current_check.success(f"🎉 Found {len(discovered)} categories with {sum(d['url_count'] for d in discovered.values())} total URLs")
    time.sleep(1)

    # Clear progress indicators
    status_text.empty()
    progress_bar.empty()
    current_check.empty()

    return dict(discovered)

def process_selected_categories(discovered_sitemaps, selected_categories, progress_container):
    """Process only the selected categories and fetch titles"""
    categorized_data = defaultdict(list)

    # Create placeholders for live updates
    status_text = progress_container.empty()
    progress_bar = progress_container.progress(0)
    stats_container = progress_container.container()
    current_url_container = progress_container.empty()

    # Calculate total sitemaps to process
    total_sitemaps = sum(len(discovered_sitemaps[cat]['sitemaps']) for cat in selected_categories if cat in discovered_sitemaps)

    status_text.markdown(f"### ⚙️ Processing {total_sitemaps} selected sitemap(s)...")

    # Statistics counters
    total_urls_processed = 0

    with stats_container:
        col1, col2, col3 = st.columns(3)
        sitemap_counter = col1.empty()
        url_counter = col2.empty()
        category_counter = col3.empty()

    processed = 0

    for category in selected_categories:
        if category not in discovered_sitemaps:
            continue

        for sitemap_url in discovered_sitemaps[category]['sitemaps']:
            sitemap_name = sitemap_url.split('/')[-1]
            current_url_container.info(f"🔄 Processing: `{sitemap_name}` ({category})")

            urls, is_index = parse_xml_sitemap(sitemap_url)
            if not is_index and urls:
                # Update stats
                sitemap_counter.metric("Sitemaps Processed", f"{processed + 1}/{total_sitemaps}")
                category_counter.metric("Categories Processing", f"{len(set(selected_categories)) - list(selected_categories).index(category)}")

                # Fetch titles for each URL
                url_data = []
                for url_idx, url in enumerate(urls):
                    title = fetch_page_title(url)
                    url_data.append({'title': title, 'url': url})
                    total_urls_processed += 1

                    # Update URL counter
                    url_counter.metric("URLs Processed", total_urls_processed)

                    # Show current URL being fetched
                    if url_idx % 5 == 0 or url_idx == len(urls) - 1:
                        short_url = url if len(url) <= 60 else url[:60] + '...'
                        current_url_container.text(f"📥 Fetching title ({url_idx + 1}/{len(urls)}): {short_url}")

                categorized_data[category].extend(url_data)
                current_url_container.success(f"✅ Completed: `{sitemap_name}` - {len(urls)} URLs")

            processed += 1
            progress_bar.progress(processed / total_sitemaps)
            time.sleep(0.1)

    # Final summary
    status_text.markdown("### ✅ Processing Complete!")
    current_url_container.success(f"🎉 Successfully processed **{total_urls_processed}** URLs from **{total_sitemaps}** sitemap(s)")
    time.sleep(1)

    # Clear progress indicators
    progress_container.empty()

    return dict(categorized_data)

def generate_html_sitemap(data, selected_categories):
    """Generate HTML sitemap from organized data"""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Sitemap</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }
        h2 {
            color: #4CAF50;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        li {
            margin: 8px 0;
        }
        a {
            color: #1a73e8;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .section {
            margin-bottom: 40px;
        }
    </style>
</head>
<body>
    <h1>HTML Sitemap</h1>
"""

    for category in selected_categories:
        if category in data:
            html += f'<div class="section">\n<h2>{category}</h2>\n<ul>\n'
            for item in data[category]:
                html += f'<li><a href="{item["url"]}">{item["title"]}</a></li>\n'
            html += '</ul>\n</div>\n'

    html += """
</body>
</html>
"""
    return html

# Input Section
st.header("📥 Step 1: Input Sitemap URLs")
sitemap_input = st.text_area(
    "Enter your XML sitemap URLs (one per line)",
    height=150,
    placeholder="https://example.com/sitemap.xml\nhttps://example.com/post-sitemap.xml\nhttps://example.com/page-sitemap.xml"
)

if st.button("🔍 Discover Sitemaps", type="primary"):
    if sitemap_input.strip():
        sitemap_urls = [url.strip() for url in sitemap_input.split('\n') if url.strip()]

        st.session_state.discovered_sitemaps = discover_sitemaps(sitemap_urls)
        st.session_state.categories = list(st.session_state.discovered_sitemaps.keys())

        # Only show success message if categories were actually found
        if st.session_state.categories:
            st.success("✅ Sitemap discovery complete! Please select categories below.")
        else:
            st.error("❌ No valid sitemaps found. Please check your URLs and try again.")
            st.info("💡 **Tips:**\n- Ensure the sitemap URLs are accessible\n- Verify the URLs are correct\n- Check if the website has a robots.txt file that lists sitemap locations")
    else:
        st.warning("⚠️ Please enter at least one sitemap URL.")

# Selection Section
if st.session_state.discovered_sitemaps:
    st.header("🎯 Step 2: Select Sitemap Sections")

    st.markdown("Choose which sitemap categories you want to include in your HTML sitemap:")

    # Display discovered categories with details
    col1, col2 = st.columns([2, 1])

    with col1:
        st.session_state.selected_categories = st.multiselect(
            "Select categories to process",
            options=st.session_state.categories,
            default=st.session_state.categories,
            help="Only selected categories will be crawled for page titles"
        )

    with col2:
        st.subheader("📊 Category Overview")
        for category in st.session_state.categories:
            info = st.session_state.discovered_sitemaps[category]
            with st.expander(f"**{category}**"):
                st.metric("Sitemaps", len(info['sitemaps']))
                st.metric("Total URLs", info['url_count'])

    # Process button
    if st.session_state.selected_categories:
        total_urls = sum(st.session_state.discovered_sitemaps[cat]['url_count'] 
                        for cat in st.session_state.selected_categories)

        st.info(f"📌 You've selected **{len(st.session_state.selected_categories)}** categories with **{total_urls}** total URLs to process")

        if st.button("🚀 Start Processing Selected Categories", type="primary"):
            progress_container = st.container()

            st.session_state.sitemap_data = process_selected_categories(
                st.session_state.discovered_sitemaps,
                st.session_state.selected_categories,
                progress_container
            )

            st.success(f"✅ Successfully processed selected categories!")
            st.balloons()
    else:
        st.warning("⚠️ Please select at least one category to process.")

# Display results and download
if st.session_state.sitemap_data:
    st.header("👁️ Step 3: Preview & Download")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📊 Final Statistics")
        for category in st.session_state.selected_categories:
            if category in st.session_state.sitemap_data:
                count = len(st.session_state.sitemap_data[category])
                st.metric(category, f"{count} URLs")

    with col2:
        st.subheader("👁️ Preview")
        for category in st.session_state.selected_categories:
            if category in st.session_state.sitemap_data:
                st.markdown(f"**{category}**")
                preview_items = st.session_state.sitemap_data[category][:5]
                for item in preview_items:
                    st.markdown(f"• [{item['title']}]({item['url']})")
                if len(st.session_state.sitemap_data[category]) > 5:
                    st.markdown(f"*...and {len(st.session_state.sitemap_data[category]) - 5} more*")
                st.markdown("---")

    # Generate and download HTML
    st.header("💾 Download HTML Sitemap")
    html_content = generate_html_sitemap(st.session_state.sitemap_data, st.session_state.selected_categories)

    st.download_button(
        label="⬇️ Download HTML Sitemap",
        data=html_content,
        file_name="sitemap.html",
        mime="text/html",
        type="primary"
    )

    with st.expander("🔍 View HTML Code"):
        st.code(html_content, language="html")


    # ENHANCED Footer with light/dark mode support
st.markdown("---")
st.markdown(
    f"""
    <div class="footer-container">
        <p>Built with ❤️ by <strong>Dhruv Pandya</strong> | XML Sitemap to HTML Sitemap Converter</p>
        </div>
    """, 
    unsafe_allow_html=True
)
