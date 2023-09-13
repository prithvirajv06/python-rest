package com.testbud.onemore.service;

import org.openqa.selenium.WebDriver;

import java.util.concurrent.TimeUnit;

public class OneMoreWebDriver {

    static WebDriver driver;

    private OneMoreWebDriver() {
        OneMoreWebDriver.getDriver();
    }

    public static WebDriver getDriver() {
        driver.manage().timeouts().pageLoadTimeout(20, TimeUnit.SECONDS);

        return driver;
    }

    public static void setDriver(WebDriver driver) {
        OneMoreWebDriver.driver = driver;
    }

    /**
     * @return
     * Getting the instance of the driver
     */
    public static WebDriver getInstance() {
        if (driver == null) {

            driver = (WebDriver) new OneMoreWebDriver();

            return driver;
        } else {

            return driver;
        }

    }
}
