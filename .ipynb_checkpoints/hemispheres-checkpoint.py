{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the executable path and initialize the chrome browser in splinter\n",
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###Visit the NASA Mars news site."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = BeautifulSoup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('ul.item_list li.slide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\"><a href=\"/news/8631/nasas-curiosity-mars-rover-takes-a-new-selfie-before-record-climb/\" target=\"_self\">NASA's Curiosity Mars Rover Takes a New Selfie Before Record Climb</a></div>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find(\"div\", class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find(\"div\", class_='content_title').get_text()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Curiosity Mars Rover Takes a New Selfie Before Record Climb\""
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Along with capturing an image before its steepest ascent ever, the robotic explorer filmed its \"selfie stick,\" or robotic arm, in action.'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_=\"article_teaser_body\").get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\"### Featured Images\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_id('full_image')\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Doug Smith\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:528: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
      "  FutureWarning,\n"
     ]
    }
   ],
   "source": [
    "# Find the more info button and click that\n",
    "browser.is_element_present_by_text('more info', wait_time=1)\n",
    "more_info_elem = browser.find_link_by_partial_text('more info')\n",
    "more_info_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/largesize/PIA17044_hires.jpg'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.select_one('figure.lede a img').get(\"src\")\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA17044_hires.jpg'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://www.jpl.nasa.gov{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>value</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-153 to 20 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              value            Earth\n",
       "description                                         \n",
       "Diameter:                  6,779 km        12,742 km\n",
       "Mass:               6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                            2                1\n",
       "Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "Length of Year:      687 Earth days      365.24 days\n",
       "Temperature:          -153 to 20 °C      -88 to 58°C"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('http://space-facts.com/mars/')[1]\n",
    "df.columns=['description', 'value', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>value</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-153 to 20 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Hemispheres site\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "hemi_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced\n",
      "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced\n",
      "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced\n",
      "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced\n"
     ]
    }
   ],
   "source": [
    "for link in hemi_soup.select('div.description a[href]'):\n",
    "    print(\"https://astrogeology.usgs.gov{}\".format(link['href']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "list_link = []\n",
    "for link in hemi_soup.select('div.description a[href]'):\n",
    "    (\"https://astrogeology.usgs.gov{}\".format(link['href']))\n",
    "    list_link.append((\"https://astrogeology.usgs.gov{}\".format(link['href'])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list_link"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit Cerberus URL\n",
    "url = list_link[0]\n",
    "url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup for Cerberus\n",
    "html = browser.html\n",
    "cerberus_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url of Cerberus\n",
    "cerb_url_rel = cerberus_soup.select_one('img.wide-image').get(\"src\")\n",
    "cerb_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL of Cerberus\n",
    "cerb_img_url = f'https://astrogeology.usgs.gov{cerb_url_rel}'\n",
    "cerb_img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Cerberus Hemisphere Enhanced'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the title for Cerberus\n",
    "cerb_title = cerberus_soup.find('h2')\n",
    "cerb_title.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit Schiaparelli URL\n",
    "url = list_link[1]\n",
    "url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup for Schiaparelli\n",
    "html = browser.html\n",
    "schia_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url of Schiaparelli\n",
    "schia_url_rel = schia_soup.select_one('img.wide-image').get(\"src\")\n",
    "schia_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL of Schiaparelli\n",
    "schia_img_url = f'https://astrogeology.usgs.gov{schia_url_rel}'\n",
    "schia_img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Schiaparelli Hemisphere Enhanced'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the title for Schiaparelli\n",
    "schia_title = schia_soup.find('h2')\n",
    "schia_title.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit Syrtis URL\n",
    "url = list_link[2]\n",
    "url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup for Syrtis Major\n",
    "html = browser.html\n",
    "syrtis_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url of Syrtis Major\n",
    "syrtis_url_rel = syrtis_soup.select_one('img.wide-image').get(\"src\")\n",
    "syrtis_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL of Syrtis Major\n",
    "syrtis_img_url = f'https://astrogeology.usgs.gov{syrtis_url_rel}'\n",
    "syrtis_img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Syrtis Major Hemisphere Enhanced'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the title for Syrtis Major\n",
    "syrtis_title = syrtis_soup.find('h2')\n",
    "syrtis_title.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit Valles Marineris URL\n",
    "url = list_link[3]\n",
    "url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup for Valles Marineris\n",
    "html = browser.html\n",
    "valles_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url of Valles Marineris\n",
    "valles_url_rel = valles_soup.select_one('img.wide-image').get(\"src\")\n",
    "valles_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL of Valles Marineris\n",
    "valles_img_url = f'https://astrogeology.usgs.gov{valles_url_rel}'\n",
    "valles_img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Valles Marineris Hemisphere Enhanced'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the title for Valles Marineris\n",
    "valles_title = valles_soup.find('h2')\n",
    "valles_title.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
