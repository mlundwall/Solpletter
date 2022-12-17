# -*- coding: utf-8 -*-
"""
Solpletter Datafil
Indeholder to dataset - 
Det første pletalle fra 1700 til 2019
Det andet plet128 tilpasset FFT med en to-potens data
@author: Mads Lundwall 2022
"""

pletalle = [\
	[1700.5,8.3],
	[1701.5,18.3],
	[1702.5,26.7],
	[1703.5,38.3],
	[1704.5,60.0],
	[1705.5,96.7],
	[1706.5,48.3],
	[1707.5,33.3],
	[1708.5,16.7],
	[1709.5,13.3],
	[1710.5,5.0],
	[1711.5,0.0],
	[1712.5,0.0],
	[1713.5,3.3],
	[1714.5,18.3],
	[1715.5,45.0],
	[1716.5,78.3],
	[1717.5,105.0],
	[1718.5,100.0],
	[1719.5,65.0],
	[1720.5,46.7],
	[1721.5,43.3],
	[1722.5,36.7],
	[1723.5,18.3],
	[1724.5,35.0],
	[1725.5,66.7],
	[1726.5,130.0],
	[1727.5,203.3],
	[1728.5,171.7],
	[1729.5,121.7],
	[1730.5,78.3],
	[1731.5,58.3],
	[1732.5,18.3],
	[1733.5,8.3],
	[1734.5,26.7],
	[1735.5,56.7],
	[1736.5,116.7],
	[1737.5,135.0],
	[1738.5,185.0],
	[1739.5,168.3],
	[1740.5,121.7],
	[1741.5,66.7],
	[1742.5,33.3],
	[1743.5,26.7],
	[1744.5,8.3],
	[1745.5,18.3],
	[1746.5,36.7],
	[1747.5,66.7],
	[1748.5,100.0],
	[1749.5,134.8],
	[1750.5,139.0],
	[1751.5,79.5],
	[1752.5,79.7],
	[1753.5,51.2],
	[1754.5,20.3],
	[1755.5,16.0],
	[1756.5,17.0],
	[1757.5,54.0],
	[1758.5,79.3],
	[1759.5,90.0],
	[1760.5,104.8],
	[1761.5,143.2],
	[1762.5,102.0],
	[1763.5,75.2],
	[1764.5,60.7],
	[1765.5,34.8],
	[1766.5,19.0],
	[1767.5,63.0],
	[1768.5,116.3],
	[1769.5,176.8],
	[1770.5,168.0],
	[1771.5,136.0],
	[1772.5,110.8],
	[1773.5,58.0],
	[1774.5,51.0],
	[1775.5,11.7],
	[1776.5,33.0],
	[1777.5,154.2],
	[1778.5,257.3],
	[1779.5,209.8],
	[1780.5,141.3],
	[1781.5,113.5],
	[1782.5,64.2],
	[1783.5,38.0],
	[1784.5,17.0],
	[1785.5,40.2],
	[1786.5,138.2],
	[1787.5,220.0],
	[1788.5,218.2],
	[1789.5,196.8],
	[1790.5,149.8],
	[1791.5,111.0],
	[1792.5,100.0],
	[1793.5,78.2],
	[1794.5,68.3],
	[1795.5,35.5],
	[1796.5,26.7],
	[1797.5,10.7],
	[1798.5,6.8],
	[1799.5,11.3],
	[1800.5,24.2],
	[1801.5,56.7],
	[1802.5,75.0],
	[1803.5,71.8],
	[1804.5,79.2],
	[1805.5,70.3],
	[1806.5,46.8],
	[1807.5,16.8],
	[1808.5,13.5],
	[1809.5,4.2],
	[1810.5,0.0],
	[1811.5,2.3],
	[1812.5,8.3],
	[1813.5,20.3],
	[1814.5,23.2],
	[1815.5,59.0],
	[1816.5,76.3],
	[1817.5,68.3],
	[1818.5,52.9],
	[1819.5,38.5],
	[1820.5,24.2],
	[1821.5,9.2],
	[1822.5,6.3],
	[1823.5,2.2],
	[1824.5,11.4],
	[1825.5,28.2],
	[1826.5,59.9],
	[1827.5,83.0],
	[1828.5,108.5],
	[1829.5,115.2],
	[1830.5,117.4],
	[1831.5,80.8],
	[1832.5,44.3],
	[1833.5,13.4],
	[1834.5,19.5],
	[1835.5,85.8],
	[1836.5,192.7],
	[1837.5,227.3],
	[1838.5,168.7],
	[1839.5,143.0],
	[1840.5,105.5],
	[1841.5,63.3],
	[1842.5,40.3],
	[1843.5,18.1],
	[1844.5,25.1],
	[1845.5,65.8],
	[1846.5,102.7],
	[1847.5,166.3],
	[1848.5,208.3],
	[1849.5,182.5],
	[1850.5,126.3],
	[1851.5,122.0],
	[1852.5,102.7],
	[1853.5,74.1],
	[1854.5,39.0],
	[1855.5,12.7],
	[1856.5,8.2],
	[1857.5,43.4],
	[1858.5,104.4],
	[1859.5,178.3],
	[1860.5,182.2],
	[1861.5,146.6],
	[1862.5,112.1],
	[1863.5,83.5],
	[1864.5,89.2],
	[1865.5,57.8],
	[1866.5,30.7],
	[1867.5,13.9],
	[1868.5,62.8],
	[1869.5,123.6],
	[1870.5,232.0],
	[1871.5,185.3],
	[1872.5,169.2],
	[1873.5,110.1],
	[1874.5,74.5],
	[1875.5,28.3],
	[1876.5,18.9],
	[1877.5,20.7],
	[1878.5,5.7],
	[1879.5,10.0],
	[1880.5,53.7],
	[1881.5,90.5],
	[1882.5,99.0],
	[1883.5,106.1],
	[1884.5,105.8],
	[1885.5,86.3],
	[1886.5,42.4],
	[1887.5,21.8],
	[1888.5,11.2],
	[1889.5,10.4],
	[1890.5,11.8],
	[1891.5,59.5],
	[1892.5,121.7],
	[1893.5,142.0],
	[1894.5,130.0],
	[1895.5,106.6],
	[1896.5,69.4],
	[1897.5,43.8],
	[1898.5,44.4],
	[1899.5,20.2],
	[1900.5,15.7],
	[1901.5,4.6],
	[1902.5,8.5],
	[1903.5,40.8],
	[1904.5,70.1],
	[1905.5,105.5],
	[1906.5,90.1],
	[1907.5,102.8],
	[1908.5,80.9],
	[1909.5,73.2],
	[1910.5,30.9],
	[1911.5,9.5],
	[1912.5,6.0],
	[1913.5,2.4],
	[1914.5,16.1],
	[1915.5,79.0],
	[1916.5,95.0],
	[1917.5,173.6],
	[1918.5,134.6],
	[1919.5,105.7],
	[1920.5,62.7],
	[1921.5,43.5],
	[1922.5,23.7],
	[1923.5,9.7],
	[1924.5,27.9],
	[1925.5,74.0],
	[1926.5,106.5],
	[1927.5,114.7],
	[1928.5,129.7],
	[1929.5,108.2],
	[1930.5,59.4],
	[1931.5,35.1],
	[1932.5,18.6],
	[1933.5,9.2],
	[1934.5,14.6],
	[1935.5,60.2],
	[1936.5,132.8],
	[1937.5,190.6],
	[1938.5,182.6],
	[1939.5,148.0],
	[1940.5,113.0],
	[1941.5,79.2],
	[1942.5,50.8],
	[1943.5,27.1],
	[1944.5,16.1],
	[1945.5,55.3],
	[1946.5,154.3],
	[1947.5,214.7],
	[1948.5,193.0],
	[1949.5,190.7],
	[1950.5,118.9],
	[1951.5,98.3],
	[1952.5,45.0],
	[1953.5,20.1],
	[1954.5,6.6],
	[1955.5,54.2],
	[1956.5,200.7],
	[1957.5,269.3],
	[1958.5,261.7],
	[1959.5,225.1],
	[1960.5,159.0],
	[1961.5,76.4],
	[1962.5,53.4],
	[1963.5,39.9],
	[1964.5,15.0],
	[1965.5,22.0],
	[1966.5,66.8],
	[1967.5,132.9],
	[1968.5,150.0],
	[1969.5,149.4],
	[1970.5,148.0],
	[1971.5,94.4],
	[1972.5,97.6],
	[1973.5,54.1],
	[1974.5,49.2],
	[1975.5,22.5],
	[1976.5,18.4],
	[1977.5,39.3],
	[1978.5,131.0],
	[1979.5,220.1],
	[1980.5,218.9],
	[1981.5,198.9],
	[1982.5,162.4],
	[1983.5,91.0],
	[1984.5,60.5],
	[1985.5,20.6],
	[1986.5,14.8],
	[1987.5,33.9],
	[1988.5,123.0],
	[1989.5,211.1],
	[1990.5,191.8],
	[1991.5,203.3],
	[1992.5,133.0],
	[1993.5,76.1],
	[1994.5,44.9],
	[1995.5,25.1],
	[1996.5,11.6],
	[1997.5,28.9],
	[1998.5,88.3],
	[1999.5,136.3],
	[2000.5,173.9],
	[2001.5,170.4],
	[2002.5,163.6],
	[2003.5,99.3],
	[2004.5,65.3],
	[2005.5,45.8],
	[2006.5,24.7],
	[2007.5,12.6],
	[2008.5,4.2],
	[2009.5,4.8],
	[2010.5,24.9],
	[2011.5,80.8],
	[2012.5,84.5],
	[2013.5,94.0],
	[2014.5,113.3],
	[2015.5,69.8],
	[2016.5,39.90],
	[2017.5,21.8],
	[2018.5,7.0],
	[2019.5,4.6]]

plet128 = [\
	[1892.5,121.7],
	[1893.5,142.0],
	[1894.5,130.0],
	[1895.5,106.6],
	[1896.5,69.4],
	[1897.5,43.8],
	[1898.5,44.4],
	[1899.5,20.2],
	[1900.5,15.7],
	[1901.5,4.6],
	[1902.5,8.5],
	[1903.5,40.8],
	[1904.5,70.1],
	[1905.5,105.5],
	[1906.5,90.1],
	[1907.5,102.8],
	[1908.5,80.9],
	[1909.5,73.2],
	[1910.5,30.9],
	[1911.5,9.5],
	[1912.5,6.0],
	[1913.5,2.4],
	[1914.5,16.1],
	[1915.5,79.0],
	[1916.5,95.0],
	[1917.5,173.6],
	[1918.5,134.6],
	[1919.5,105.7],
	[1920.5,62.7],
	[1921.5,43.5],
	[1922.5,23.7],
	[1923.5,9.7],
	[1924.5,27.9],
	[1925.5,74.0],
	[1926.5,106.5],
	[1927.5,114.7],
	[1928.5,129.7],
	[1929.5,108.2],
	[1930.5,59.4],
	[1931.5,35.1],
	[1932.5,18.6],
	[1933.5,9.2],
	[1934.5,14.6],
	[1935.5,60.2],
	[1936.5,132.8],
	[1937.5,190.6],
	[1938.5,182.6],
	[1939.5,148.0],
	[1940.5,113.0],
	[1941.5,79.2],
	[1942.5,50.8],
	[1943.5,27.1],
	[1944.5,16.1],
	[1945.5,55.3],
	[1946.5,154.3],
	[1947.5,214.7],
	[1948.5,193.0],
	[1949.5,190.7],
	[1950.5,118.9],
	[1951.5,98.3],
	[1952.5,45.0],
	[1953.5,20.1],
	[1954.5,6.6],
	[1955.5,54.2],
	[1956.5,200.7],
	[1957.5,269.3],
	[1958.5,261.7],
	[1959.5,225.1],
	[1960.5,159.0],
	[1961.5,76.4],
	[1962.5,53.4],
	[1963.5,39.9],
	[1964.5,15.0],
	[1965.5,22.0],
	[1966.5,66.8],
	[1967.5,132.9],
	[1968.5,150.0],
	[1969.5,149.4],
	[1970.5,148.0],
	[1971.5,94.4],
	[1972.5,97.6],
	[1973.5,54.1],
	[1974.5,49.2],
	[1975.5,22.5],
	[1976.5,18.4],
	[1977.5,39.3],
	[1978.5,131.0],
	[1979.5,220.1],
	[1980.5,218.9],
	[1981.5,198.9],
	[1982.5,162.4],
	[1983.5,91.0],
	[1984.5,60.5],
	[1985.5,20.6],
	[1986.5,14.8],
	[1987.5,33.9],
	[1988.5,123.0],
	[1989.5,211.1],
	[1990.5,191.8],
	[1991.5,203.3],
	[1992.5,133.0],
	[1993.5,76.1],
	[1994.5,44.9],
	[1995.5,25.1],
	[1996.5,11.6],
	[1997.5,28.9],
	[1998.5,88.3],
	[1999.5,136.3],
	[2000.5,173.9],
	[2001.5,170.4],
	[2002.5,163.6],
	[2003.5,99.3],
	[2004.5,65.3],
	[2005.5,45.8],
	[2006.5,24.7],
	[2007.5,12.6],
	[2008.5,4.2],
	[2009.5,4.8],
	[2010.5,24.9],
	[2011.5,80.8],
	[2012.5,84.5],
	[2013.5,94.0],
	[2014.5,113.3],
	[2015.5,69.8],
	[2016.5,39.90],
	[2017.5,21.8],
	[2018.5,7.0],
	[2019.5,4.6]]
