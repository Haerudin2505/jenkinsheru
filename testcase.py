from selenium import webdriver
def test_setup():
	global driver
	driver=webdriver.Chrome(executable_path="D:/Master/chromedriver_win32/chromedriver.exe");
	driver.maximize_window();
	
def test_form_entry():
	driver.get("https://localhost/form.php");
	driver.find_element_by_name("nip").send_keys("12345");
	driver.find_element_by_name("nama").send_keys("Heru");
	driver.find_element_by_name("nik").send_keys("07070433");
	driver.find_element_by_name("alamat").send_keys("tangerang");
	driver.find_element_by_name("perusahaan").send_keys("piktip");
	driver.find_element_by_name("tanggal").send_keys("01/01/2021");
	driver.find_element_by_name("divisi").send_keys("HRD");
	driver.find_element_by_name("posisi").send_keys("BOS");
	driver.find_element_by_name("gaji").send_keys("1000000");
	driver.find_element_by_name("atasan").send_keys("SAYA AJA");
	driver.find_element_by_name("submit").click();

def test_cleanup():
	driver.close();
	driver.quit();
	print("Test selesai ...");