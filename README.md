# 🗺️ XML to HTML Sitemap Converter

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green)](https://github.com/dhruvpandyadp/xml-sitemap-converter)

**XML to HTML Sitemap Converter** is a powerful, intuitive web application that transforms your XML sitemaps into beautifully organized, user-friendly HTML sitemaps. Perfect for improving website navigation, SEO, and user experience with automated title fetching, smart categorization, and elegant formatting.

![Sitemap Processing](https://img.shields.io/badge/Sitemap%20Processing-Automated-brightgreen)
![Categories](https://img.shields.io/badge/Smart%20Categorization-7%2B%20Types-blue)
![Title Fetching](https://img.shields.io/badge/Title%20Fetching-Automatic-orange)

## ✨ Key Features

### 🚀 **Intelligent Sitemap Discovery**
- 🔍 **Automatic Index Detection** - Automatically discovers and processes sitemap indexes
- 📊 **Smart Categorization** - Organizes sitemaps into Post, Page, Category, Tag, Author, Product, and Other types
- 🗂 **Multi-Sitemap Support** - Process multiple XML sitemaps simultaneously
- 📈 **URL Counting** - Pre-analysis of URL counts before processing
- ⚡ **Fast Discovery** - Quick scanning of sitemap structures without full crawling

### 🎯 **Selective Processing**
- ✅ **Category Selection** - Choose which sitemap categories to include
- 📊 **Preview Statistics** - View URL counts per category before processing
- 💡 **Smart Defaults** - All categories selected by default for quick conversion
- 🔢 **Progress Tracking** - Real-time updates during processing
- 📋 **Category Overview** - Detailed breakdown of sitemaps and URLs per category

### 🖼️ **Automated Title Fetching**
- 🌐 **Live Title Extraction** - Automatically fetches page titles from URLs
- 🔄 **Real-time Progress** - Live updates showing current URL being processed
- 📊 **Statistics Dashboard** - Track sitemaps processed, URLs fetched, and categories completed
- ⏱ **Efficient Processing** - Optimized for handling large sitemaps
- 🛡️ **Error Handling** - Graceful fallback to URLs when titles unavailable

### 💻 **Professional HTML Output**
- 🎨 **Clean Design** - Modern, responsive HTML with professional styling
- 📱 **Mobile-Friendly** - Optimized for all devices and screen sizes
- 🗂️ **Organized Structure** - Clear sections for each sitemap category
- 🔗 **Clickable Links** - Direct navigation to all pages
- 📄 **Download Ready** - Instant download as .html file

### 🛠️ **User-Friendly Interface**
- 🎯 **3-Step Process** - Simple workflow: Input → Select → Download
- 📊 **Live Statistics** - Real-time metrics during processing
- 🎉 **Visual Feedback** - Progress bars, status updates, and celebrations
- 👁️ **Preview Mode** - See results before downloading
- 📥 **One-Click Download** - Export HTML sitemap instantly

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dhruvpandyadp/XML-to-HTML-Sitemap-Converter.git
   ```
   ```bash
   cd XML-to-HTML-Sitemap-Converter
   ```

2. **Install dependencies:**
   ```bash
   pip3 install streamlit requests beautifulsoup4
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and go to `http://localhost:8501`

## 💻 Usage

### Step 1: Input Sitemap URLs
1. Enter your XML sitemap URLs (one per line)
2. Examples:
   ```
   https://example.com/sitemap.xml
   https://example.com/post-sitemap.xml
   https://example.com/page-sitemap.xml
   ```
3. Click **"🔍 Discover Sitemaps"**

### Step 2: Select Categories
1. Review discovered sitemap categories
2. View statistics for each category:
   - Number of sitemaps
   - Total URL count
3. Select which categories to process
4. Click **"🚀 Start Processing Selected Categories"**

### Step 3: Preview & Download
1. View final statistics and preview
2. Review sample URLs from each category
3. Click **"⬇️ Download HTML Sitemap"**
4. Optional: View HTML code before downloading

## 📊 Supported Sitemap Types

The converter automatically categorizes sitemaps into:

1. **Post Sitemap** - Blog posts and articles
2. **Page Sitemap** - Static pages and content
3. **Category Sitemap** - Category archives
4. **Tag Sitemap** - Tag archives
5. **Author Sitemap** - Author pages
6. **Product Sitemap** - E-commerce products
7. **Other Sitemap** - Miscellaneous content

## 🎨 Features in Detail

### Intelligent Sitemap Discovery
```
Input: https://example.com/sitemap.xml
↓
Discovers: Sitemap Index with 5 sub-sitemaps
↓
Analyzes: Each sub-sitemap for category and URL count
↓
Result: Organized list of all sitemaps by category
```

### Selective Processing
```
Discovered:
├── Post Sitemap (450 URLs)
├── Page Sitemap (25 URLs)
├── Category Sitemap (15 URLs)
└── Product Sitemap (200 URLs)

Selected: Post Sitemap + Page Sitemap
↓
Processes: Only 475 URLs instead of 690
↓
Result: Faster processing with targeted output
```

### Title Fetching Process
```
For each URL:
1. Fetch webpage content
2. Extract <title> tag
3. Fallback to URL if title unavailable
4. Display real-time progress
5. Update statistics dashboard
```

## 📊 Example Output

### Generated HTML Sitemap Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML Sitemap</title>
    <!-- Professional CSS styling included -->
</head>
<body>
    <h1>HTML Sitemap</h1>
    
    <div class="section">
        <h2>Post Sitemap</h2>
        <ul>
            <li><a href="...">Article Title 1</a></li>
            <li><a href="...">Article Title 2</a></li>
            <!-- More posts -->
        </ul>
    </div>
    
    <div class="section">
        <h2>Page Sitemap</h2>
        <ul>
            <li><a href="...">About Us</a></li>
            <li><a href="...">Contact</a></li>
            <!-- More pages -->
        </ul>
    </div>
</body>
</html>
```

### Sample Statistics Display
| Category | Sitemaps | URLs | Status |
|----------|----------|------|--------|
| Post Sitemap | 3 | 450 | ✅ Processed |
| Page Sitemap | 1 | 25 | ✅ Processed |
| Category Sitemap | 1 | 15 | ⏭️ Skipped |
| Product Sitemap | 2 | 200 | ⏭️ Skipped |

## 🛠️ Technical Details

### Built With
- **[Streamlit](https://streamlit.io/)** - Modern web app framework for Python
- **[Requests](https://requests.readthedocs.io/)** - HTTP library for fetching content
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** - HTML parsing and title extraction
- **[xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)** - XML sitemap parsing
- **Python 3.7+** - Core programming language

### Architecture
- **URL Normalization**: Handles various URL formats (with/without https://)
- **Namespace Handling**: Supports standard sitemap XML namespaces
- **Index Detection**: Automatically identifies sitemap indexes vs regular sitemaps
- **Smart Categorization**: Pattern-based sitemap type detection
- **Progress Tracking**: Real-time updates during processing
- **Session State**: Maintains data across Streamlit reruns

### Performance Features
- **Selective Processing**: Only fetch titles for selected categories
- **Batch Updates**: Efficient progress display (updates every 5 URLs)
- **Timeout Handling**: 5-second timeout for title fetching
- **Error Recovery**: Continues processing if individual URLs fail
- **Memory Efficient**: Processes URLs sequentially

## 📱 Browser Compatibility

| Browser | Discovery | Selection | Processing | Download |
|---------|-----------|-----------|------------|----------|
| Chrome | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Firefox | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Safari | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Edge | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Mobile Chrome | ✅ Full | ✅ Responsive | ✅ Full | ✅ Full |
| Mobile Safari | ✅ Full | ✅ Responsive | ✅ Full | ✅ Full |

## 🎯 Use Cases

### **SEO Optimization**
```
Scenario: Improve website navigation and SEO
Action: Convert XML sitemap to user-friendly HTML
Result: Clean, organized HTML sitemap with page titles
Benefit: Better user experience and search engine crawling
```

### **Website Migration**
```
Scenario: Moving to new CMS or domain
Action: Generate HTML sitemap from existing XML sitemaps
Result: Complete catalog of all pages with titles
Benefit: Easy content inventory and migration planning
```

## 🚀 Advanced Features

### Multi-Sitemap Processing
```python
# Supports multiple input formats:
https://example.com/sitemap.xml          # Single sitemap
https://example.com/sitemap_index.xml    # Sitemap index
https://example.com/post-sitemap1.xml    # Multiple specific sitemaps
https://example.com/post-sitemap2.xml
https://example.com/page-sitemap.xml
```

### Smart Category Detection
```python
# Automatically recognizes patterns:
post-sitemap.xml        → Post Sitemap
page-sitemap.xml        → Page Sitemap
category-sitemap.xml    → Category Sitemap
product-sitemap1.xml    → Product Sitemap
custom-sitemap.xml      → Other Sitemap
```

### Real-Time Processing Updates
```
Live Display:
🔄 Processing: post-sitemap1.xml (Post Sitemap)
📥 Fetching title (123/450): https://example.com/article...
✅ Completed: post-sitemap1.xml - 450 URLs

Statistics:
Sitemaps Processed: 3/5
URLs Processed: 675
Categories Processing: 2
```

## 📈 Performance Metrics

### Processing Speed
- **Small Sitemap** (< 50 URLs): ~30 seconds
- **Medium Sitemap** (50-500 URLs): 2-10 minutes
- **Large Sitemap** (500+ URLs): 10-30 minutes

*Note: Speed depends on website response times and network conditions*

### Scalability
- ✅ **Tested with**: 1000+ URLs successfully
- ✅ **Multiple sitemaps**: Up to 10 sitemap files
- ✅ **Memory efficient**: Processes URLs sequentially
- ✅ **Error resilient**: Continues on individual failures

## 🎨 Interface Highlights

### Modern Design
- **Gradient Headers**: Purple gradient for visual appeal
- **Light/Dark Mode**: Automatic theme support
- **Responsive Layout**: Optimized for all screen sizes
- **Clean Typography**: Easy-to-read fonts and spacing

### Progress Indicators
- **Discovery Phase**: Shows sitemap scanning progress
- **Processing Phase**: Live URL fetching updates
- **Statistics Dashboard**: Real-time metrics display
- **Status Messages**: Clear success/error indicators

### User Experience
- **3-Step Workflow**: Clear, logical process flow
- **Visual Feedback**: Balloons and success messages
- **Expandable Sections**: Detailed info without clutter
- **Preview Mode**: See results before downloading

## 🔧 Configuration Options

### Timeout Settings
```python
# Adjust in fetch_page_title() function
timeout=5  # Seconds to wait for page response
```

### Processing Delays
```python
# Adjust in process_selected_categories()
time.sleep(0.1)  # Delay between sitemap processing
```

### Display Updates
```python
# Adjust in process_selected_categories()
if url_idx % 5 == 0:  # Update display every 5 URLs
```

## 📦 Dependencies

```txt
streamlit>=1.0.0
requests>=2.25.0
beautifulsoup4>=4.9.0
```

Install all dependencies:
```bash
pip3 install -r requirements.txt
```

## 🐛 Troubleshooting

### Issue: "Error parsing sitemap"
**Solution**: Verify the sitemap URL is accessible and contains valid XML

### Issue: Slow title fetching
**Solution**: Some websites have slow response times; adjust timeout settings

### Issue: Missing titles
**Solution**: URLs are used as fallback when title extraction fails

### Issue: Connection timeout
**Solution**: Check internet connection and firewall settings

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Built with ❤️ by Dhruv Pandya**

- GitHub: [@dhruvpandyadp](https://github.com/dhruvpandyadp)
- LinkedIn: [Dhruv Pandya](https://linkedin.com/in/dhruvpandyadp)

## 🙏 Acknowledgments

- Streamlit team for the excellent web framework
- BeautifulSoup developers for HTML parsing capabilities
- Python Requests library for reliable HTTP handling
- Open source community for inspiration and feedback

---

## 🚀 Ready to Convert Your Sitemaps?

**Transform XML to HTML in minutes!**

```bash
# Get started in under a minute
git clone https://github.com/dhruvpandyadp/XML-to-HTML-Sitemap-Converter.git
cd XML-to-HTML-Sitemap-Converter
pip3 install streamlit requests beautifulsoup4
streamlit run app.py
```

### What You'll Get:
- 🗺️ **Professional HTML Sitemaps** with clean design
- 🔍 **Automatic Title Fetching** from live pages
- 📊 **Smart Categorization** of content types
- ⚡ **Fast Processing** with real-time progress
- 📥 **One-Click Download** of formatted HTML
- 🎯 **Selective Processing** for efficiency

**Create beautiful HTML sitemaps for your website today!**

---

## 💡 Pro Tips

1. **Start Small**: Test with a single sitemap before processing all
2. **Check Preview**: Review the preview before downloading
3. **Select Wisely**: Only process categories you need
4. **Verify URLs**: Ensure sitemap URLs are accessible
5. **Save Settings**: Keep your sitemap URLs for future updates

---
⭐ **If this tool helps you create better sitemaps, please give it a star!** ⭐

[![GitHub stars](https://img.shields.io/github/stars/dhruvpandyadp/XML-to-HTML-Sitemap-Converter.svg?style=social&label=Star)](https://github.com/dhruvpandyadp/XML-to-HTML-Sitemap-Converter)
