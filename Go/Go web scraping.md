# Web Scraping

## Parse static pages

## Interact with dynamic pages

### Selenium

#### Install requirements

1. Detect latest package from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
1. Execute
    ```   
    wget https://chromedriver.googlecode.com/files/chromedriver_linux64_2.3.zip
    unzip chromedriver_linux64.zip
    sudo cp chromedriver /usr/bin/chromedriver
    sudo chown root /usr/bin/chromedriver
    sudo chmod +x /usr/bin/chromedriver
    sudo chmod 755 /usr/bin/chromedriver
    ```

## Code

```go

// Run Chrome browser
service, err := selenium.NewChromeDriverService("chromedriver", 4444)
if err != nil {
	panic(err)
}
defer service.Stop()

caps := selenium.Capabilities{}
caps.AddChrome(chrome.Capabilities{Args: []string{
	"window-size=1920x1080",
	"--no-sandbox",
	"--disable-dev-shm-usage",
	"disable-gpu",
	"--headless", // comment out this line to see the browser
}})

driver, err := selenium.NewRemote(caps, "")
if err != nil {
	panic(err)
}

driver.Get("https://www.speakup.it/magazines")
```
    
