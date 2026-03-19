import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import countries

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Colors:
    PRIMARY = "#4361ee"
    SECONDARY = "#3f37c9"
    ACCENT = "#4cc9f0"
    SUCCESS = "#06d6a0"
    WARNING = "#ffd166"
    DANGER = "#ef476f"
    DARK = "#2b2d42"
    LIGHT = "#f8f9fa"
    GRAY = "#6c757d"


class ModernButton(QPushButton):
    def __init__(self, text, primary=True, parent=None):
        super().__init__(text, parent)
        self.primary = primary
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(40)
        self.setMinimumWidth(100)
        self._setup_style()

    def _setup_style(self):
        if self.primary:
            self.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                               stop:0 #4361ee, stop:1 #3a0ca3);
                    color: white;
                    border: none;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 14px;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                               stop:0 #4895ef, stop:1 #4361ee);
                }
                QPushButton:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                               stop:0 #3a0ca3, stop:1 #2b2d42);
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background: white;
                    color: #2b2d42;
                    border: 2px solid #e9ecef;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 14px;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background: #f8f9fa;
                    border-color: #4361ee;
                }
                QPushButton:pressed {
                    background: #e9ecef;
                }
            """)


class ModernSearchBar(QLineEdit):
    def __init__(self, placeholder, parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setFixedHeight(45)
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e9ecef;
                border-radius: 12px;
                padding: 10px 15px 10px 45px;
                font-size: 14px;
                background: white;
                selection-background-color: #4361ee;
            }
            QLineEdit:focus {
                border-color: #4361ee;
            }
        """)

        self.icon_label = QLabel(self)
        self.icon_label.setGeometry(15, 12, 20, 20)
        self.icon_label.setText("🔍")
        self.icon_label.setStyleSheet("color: #6c757d; font-size: 16px; background: transparent;")


class CountryCard(QFrame):
    clicked = pyqtSignal(object)

    def __init__(self, country_data, parent=None):
        super().__init__(parent)
        self.country_data = country_data
        self.setup_ui()
        self.setCursor(Qt.PointingHandCursor)

    def setup_ui(self):
        self.setFixedHeight(100)
        self.setStyleSheet("""
            CountryCard {
                background: white;
                border-radius: 15px;
                border: 1px solid #e9ecef;
            }
            CountryCard:hover {
                background: #f8f9fa;
                border-color: #4361ee;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(15)

        flag_container = QFrame()
        flag_container.setFixedSize(60, 60)
        flag_container.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                       stop:0 #f8f9fa, stop:1 #e9ecef);
            border-radius: 30px;
        """)
        flag_layout = QVBoxLayout(flag_container)
        flag_layout.setContentsMargins(0, 0, 0, 0)

        flag = QLabel("🌍")
        flag.setStyleSheet("font-size: 30px; background: transparent;")
        flag.setAlignment(Qt.AlignCenter)
        flag_layout.addWidget(flag)

        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(5)

        name = QLabel(f"<b>{self.country_data['name']}</b>")
        name.setStyleSheet("font-size: 16px; color: #2b2d42;")

        capital = self.country_data.get('capital', 'N/A')
        region = self.country_data.get('region', 'N/A')
        details = QLabel(f"{capital} • {region}")
        details.setStyleSheet("font-size: 13px; color: #6c757d;")

        pop = self.country_data.get('population', 0)
        gdp = self.country_data.get('gdp', 0)
        stats = QLabel(f"👥 {pop:,}  |  💰 ${gdp}B")
        stats.setStyleSheet("font-size: 12px; color: #4361ee; font-weight: bold;")

        info_layout.addWidget(name)
        info_layout.addWidget(details)
        info_layout.addWidget(stats)

        arrow = QLabel("→")
        arrow.setStyleSheet("font-size: 20px; color: #6c757d;")

        layout.addWidget(flag_container)
        layout.addWidget(info_widget, 1)
        layout.addWidget(arrow)

    def mousePressEvent(self, event):
        self.clicked.emit(self.country_data)
        super().mousePressEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Data Viewer")
        self.setGeometry(100, 100, 1100, 800)
        self.setMinimumSize(900, 600)

        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                           stop:0 #f8f9fa, stop:1 #e9ecef);
            }
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background: #f8f9fa;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #6c757d;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background: #4361ee;
            }
        """)

        self.setup_ui()
        self.load_countries()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        header = QFrame()
        header.setFixedHeight(150)
        header.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                       stop:0 #4361ee, stop:1 #3a0ca3);
            border-radius: 20px;
        """)
        header_layout = QVBoxLayout(header)

        title = QLabel("🌍 World Data Viewer")
        title.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title)

        subtitle = QLabel("Important data, all in one place")
        subtitle.setStyleSheet("color: rgba(255,255,255,0.8); font-size: 16px;")
        subtitle.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(subtitle)

        layout.addWidget(header)

        search_container = QFrame()
        search_container.setStyleSheet("background: transparent;")
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(0, 0, 0, 0)

        self.search = ModernSearchBar("Search by country name or code...")
        search_layout.addWidget(self.search)

        self.clear_btn = ModernButton("Clear", primary=False)
        self.clear_btn.clicked.connect(self.clear_search)
        search_layout.addWidget(self.clear_btn)

        layout.addWidget(search_container)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_widget)
        self.grid_layout.setSpacing(15)
        self.grid_layout.setAlignment(Qt.AlignTop)

        scroll.setWidget(self.grid_widget)
        layout.addWidget(scroll)

        self.status = QStatusBar()
        self.status.setStyleSheet("""
            QStatusBar {
                background: white;
                color: #6c757d;
                border-top: 1px solid #e9ecef;
            }
        """)
        self.setStatusBar(self.status)
        self.status.showMessage("")

        self.search.textChanged.connect(self.filter_countries)

    def load_countries(self):
        self.all_countries = countries.get_all_countries()
        self.filtered_countries = self.all_countries.copy()
        self.display_countries()

    def display_countries(self):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        for i, country in enumerate(self.filtered_countries):
            card = CountryCard(country)
            card.clicked.connect(self.show_details)
            row = i // 2
            col = i % 2
            self.grid_layout.addWidget(card, row, col)

    def filter_countries(self):
        query = self.search.text().lower()
        if not query:
            self.filtered_countries = self.all_countries.copy()
        else:
            self.filtered_countries = [
                c for c in self.all_countries
                if query in c['name'].lower() or query in c['code'].lower()
            ]
        self.display_countries()

    def clear_search(self):
        self.search.clear()

    def show_details(self, country):
        self.detail = DetailWindow(country, self)
        self.detail.show()


class DetailWindow(QMainWindow):
    def __init__(self, country, parent=None):
        super().__init__(parent)
        self.country = country
        self.setWindowTitle(country['name'])
        self.setGeometry(200, 200, 1000, 800)
        self.setMinimumSize(900, 700)

        self.setStyleSheet("""
            QMainWindow {
                background: #f8f9fa;
            }
        """)

        self.setup_ui()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        header = QFrame()
        header.setFixedHeight(80)
        header.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                       stop:0 #4361ee, stop:1 #3a0ca3);
            border-radius: 12px;
        """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 5, 15, 5)
        header_layout.setSpacing(10)

        flag_container = QFrame()
        flag_container.setFixedSize(40, 40)
        flag_container.setStyleSheet("""
            background: white;
            border-radius: 20px;
        """)
        flag_layout = QVBoxLayout(flag_container)
        flag_layout.setContentsMargins(0, 0, 0, 0)

        flag = QLabel("🌍")
        flag.setStyleSheet("font-size: 20px; background: transparent;")
        flag.setAlignment(Qt.AlignCenter)
        flag_layout.addWidget(flag)

        name = QLabel(self.country['name'])
        name.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")

        header_layout.addWidget(flag_container)
        header_layout.addWidget(name, 1)

        layout.addWidget(header)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBar().setExpanding(True)
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: none;
                background: white;
                border-radius: 12px;
                margin-top: 10px;
            }
            QTabBar::tab {
                background: transparent;
                color: #6c757d;
                border: none;
                padding: 12px 0;
                font-weight: bold;
                font-size: 14px;
            }
            QTabBar::tab:selected {
                color: #4361ee;
                border-bottom: 3px solid #4361ee;
            }
            QTabBar::tab:hover:!selected {
                color: #3a0ca3;
                background: #f1f3f5;
            }
        """)

        self.create_overview_tab()
        self.create_exports_tab()

        layout.addWidget(self.tabs)

        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet("background: white; color: #6c757d; border-top: 1px solid #e9ecef;")
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage(f"")

    def create_overview_tab(self):
        tab = QWidget()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: transparent; border: none; }")

        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        grid = QGridLayout()
        grid.setSpacing(10)

        def create_info_card(icon, label, value):
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background: #f8f9fa;
                    border-radius: 12px;
                }
            """)
            card.setMinimumHeight(80)

            card_layout = QFormLayout(card)
            card_layout.setSpacing(5)
            card_layout.setContentsMargins(12, 12, 12, 12)
            card_layout.setLabelAlignment(Qt.AlignLeft)
            card_layout.setFormAlignment(Qt.AlignRight)

            title_text = f"{icon} {label}"
            title_label = QLabel(title_text)
            title_label.setStyleSheet("color: #6c757d; font-size: 13px; background: transparent;")

            value_label = QLabel(value)
            value_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2b2d42; background: transparent;")
            value_label.setAlignment(Qt.AlignRight)
            value_label.setWordWrap(True)

            card_layout.addRow(title_label, value_label)

            return card

        pop = self.country.get('population', 0)
        gdp = self.country.get('gdp', 0)
        area = self.country.get('area', 0)
        capital = self.country.get('capital', 'N/A')

        pop_str = f"{pop:,}" if pop else "N/A"
        gdp_str = f"${gdp}B" if gdp else "N/A"
        area_str = f"{area:,} km²" if area else "N/A"
        capital_str = capital if capital else "N/A"

        grid.addWidget(create_info_card("👥", "Population", pop_str), 0, 0)
        grid.addWidget(create_info_card("💰", "GDP", gdp_str), 0, 1)
        grid.addWidget(create_info_card("🗺️", "Area", area_str), 1, 0)
        grid.addWidget(create_info_card("🏛️", "Capital", capital_str), 1, 1)

        layout.addLayout(grid)

        if self.country.get('languages'):
            lang_card = create_info_card("🗣️", "Languages", "\n".join([f"• {l}" for l in self.country['languages']]))
            layout.addWidget(lang_card)

        if self.country.get('currencies'):
            curr_texts = []
            for curr in self.country['currencies']:
                if isinstance(curr, dict):
                    name = curr.get('name', 'Unknown')
                    symbol = curr.get('symbol', '')
                    curr_texts.append(f"• {name} ({symbol})")
                else:
                    curr_texts.append(f"• {curr}")
            curr_card = create_info_card("💵", "Currencies", "\n".join(curr_texts))
            layout.addWidget(curr_card)

        if self.country.get('timezones'):
            tz_text = ", ".join(self.country['timezones'])
            tz_card = create_info_card("⏰", "Time Zones", tz_text)
            layout.addWidget(tz_card)

        layout.addStretch()
        scroll.setWidget(content)

        tab_layout = QVBoxLayout(tab)
        tab_layout.setContentsMargins(0, 0, 0, 0)
        tab_layout.addWidget(scroll)

        self.tabs.addTab(tab, "📊 Overview")

    def create_exports_tab(self):
        tab = QWidget()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: transparent; border: none; }")

        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        header_frame = QFrame()
        header_frame.setStyleSheet("QFrame { background: #f8f9fa; border-radius: 12px; padding: 15px; }")
        header_layout = QVBoxLayout(header_frame)
        header_layout.setSpacing(5)

        header_title = QLabel("📦 Export Composition")
        header_title.setStyleSheet("font-weight: bold; color: #2b2d42; font-size: 16px;")
        header_layout.addWidget(header_title)

        exports_data = self.country.get('exports', [])
        if exports_data:
            total = sum(item.get('value', 0) for item in exports_data)
            header_total = QLabel(f"Total Exports: ${total:.1f} Billion")
            header_total.setStyleSheet("color: #6c757d; font-size: 13px;")
            header_layout.addWidget(header_total)
        else:
            header_total = QLabel("No export data available")
            header_total.setStyleSheet("color: #6c757d; font-size: 13px;")
            header_layout.addWidget(header_total)

        layout.addWidget(header_frame)

        if exports_data:
            colors = ["#4361ee", "#4cc9f0", "#f72585", "#7209b7", "#06d6a0", "#ffd166", "#fb8500", "#8338ec"]

            for i, item in enumerate(exports_data):
                color = colors[i % len(colors)]

                item_frame = QFrame()
                item_frame.setStyleSheet("QFrame { background: #f8f9fa; border-radius: 12px; padding: 15px; }")
                item_layout = QVBoxLayout(item_frame)
                item_layout.setSpacing(8)

                top_row = QHBoxLayout()

                product_label = QLabel(item.get('product', 'Unknown'))
                product_label.setStyleSheet("font-weight: bold; color: #2b2d42; font-size: 14px;")

                percent_label = QLabel(f"{item.get('percentage', 0)}%")
                percent_label.setStyleSheet(f"color: {color}; font-weight: bold; font-size: 14px;")

                top_row.addWidget(product_label)
                top_row.addStretch()
                top_row.addWidget(percent_label)

                progress_bar = QProgressBar()
                progress_bar.setRange(0, 100)
                progress_bar.setValue(int(item.get('percentage', 0)))
                progress_bar.setTextVisible(False)
                progress_bar.setFixedHeight(10)
                progress_bar.setStyleSheet(f"""
                    QProgressBar {{
                        border: none;
                        background: #e9ecef;
                        border-radius: 5px;
                    }}
                    QProgressBar::chunk {{
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                                   stop:0 {color}, stop:1 #4cc9f0);
                        border-radius: 5px;
                    }}
                """)

                value_label = QLabel(f"Value: ${item.get('value', 0)} Billion")
                value_label.setStyleSheet("color: #6c757d; font-size: 11px;")
                value_label.setAlignment(Qt.AlignRight)

                item_layout.addLayout(top_row)
                item_layout.addWidget(progress_bar)
                item_layout.addWidget(value_label)

                layout.addWidget(item_frame)

        layout.addStretch()
        scroll.setWidget(content)

        tab_layout = QVBoxLayout(tab)
        tab_layout.setContentsMargins(0, 0, 0, 0)
        tab_layout.addWidget(scroll)

        self.tabs.addTab(tab, "📈 Exports")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 9))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())