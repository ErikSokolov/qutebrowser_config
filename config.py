# Load autoconfig settings (do not load GUI-based configurations)
config.load_autoconfig(False)

# --- 2x Scaling Settings ---
# Set web content zoom to 200% (2x scaling)
c.zoom.default = '200%'

# Enable high-DPI scaling for the UI
c.qt.highdpi = True

# --- Dark Mode Settings ---
# Enable dark mode for web pages
c.colors.webpage.darkmode.enabled = True

# --- UI Dark Mode Colors ---
# Dark mode for the status bar
c.colors.statusbar.normal.bg = '#000000'
c.colors.statusbar.normal.fg = '#ffffff'
c.colors.statusbar.command.bg = '#000000'
c.colors.statusbar.command.fg = '#ffffff'

# Dark mode for the tab bar
c.colors.tabs.bar.bg = '#000000'
c.colors.tabs.odd.bg = '#222222'
c.colors.tabs.even.bg = '#222222'
c.colors.tabs.odd.fg = '#ffffff'
c.colors.tabs.even.fg = '#ffffff'
c.colors.tabs.selected.odd.bg = '#444444'
c.colors.tabs.selected.even.bg = '#444444'
c.colors.tabs.selected.odd.fg = '#ffffff'
c.colors.tabs.selected.even.fg = '#ffffff'

# --- Other Useful Settings ---
# Set the start page (can be a blank page or a URL of your choice)
c.url.start_pages = ['about:blank']

# Default search engine (DuckDuckGo as an example)
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}

# Enable the status bar for useful information
c.statusbar.show = 'always'

# Set the default behavior for opening new tabs (use 'blank' for a blank tab)
c.tabs.select_on_remove = 'next'

# Enable smooth scrolling for better navigation
c.scrolling.smooth = True

c.url.start_pages = 'https://chatgpt.com/'

