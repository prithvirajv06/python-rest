package com.testbud.onemore.service;

import com.testbud.onemore.model.OneMoreTestSuite;
import com.testbud.onemore.model.OneMoreUiTestCase;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.springframework.stereotype.Service;

import java.lang.reflect.Method;
import java.time.Duration;
import java.util.List;
import java.util.Set;

@Service
public class OneMoreExecutionServiceImpl implements OneMoreExecutionService {


    List<WebElement> listOfElements;

    @Override
    public void executeTestSuite(OneMoreTestSuite oneMoreTestSuite) {
        for (OneMoreUiTestCase mtcTestCaseForExe : oneMoreTestSuite.getMascotaTestCaseList()) {
            methodExecutor(mtcTestCaseForExe);
        }
    }


    public void methodExecutor(OneMoreUiTestCase testCase) {

        switch (testCase.getObjectLocatorType()) {

            case "ID":
                findElementById(testCase.getObjectLocator());
                break;
            case "NAME":
                findElementByName(testCase.getObjectLocator());
                break;
            case "XPATH":
                findElementByXpath(testCase.getObjectLocator());
                break;
            case "CSS":
                findElementByCssSelector(testCase.getObjectLocator());
                break;
            default:
                break;
        }
        executeAction(testCase);

    }

    public void executeAction(OneMoreUiTestCase testCase) {
        switch (testCase.getActions()) {
            case "TYPE":
                enterText(testCase.getActionValue());
            case "CLICK":
                click();
            case "SELECT":
                selectDropDownByVisibleText(testCase.getActionValue());
            case "AUTOCOMPLETE_SELECT":
                selectFromAutoComplete(testCase.getActionValue());
        }
    }


    /**
     * Find Element By CSS
     */
    private void findElementByCssSelector(String objectLocators) {

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        wait.until(ExpectedConditions.visibilityOfElementLocated(By
                .cssSelector(objectLocators)));

        List<WebElement> list1 = OneMoreWebDriver.getInstance().findElements(
                By.cssSelector(objectLocators));
        listOfElements = list1;

    }


    /**
     * Find Element By CSS
     *
     * @return
     */
    private List<WebElement> findElementByTextContent(String objectLocators) {

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        // located element with contains()
        WebElement m = OneMoreWebDriver.getDriver().findElement(By.xpath("//*[contains(text()," + objectLocators + ")]"));
        wait.until(ExpectedConditions.visibilityOfElementLocated(By
                .cssSelector(objectLocators)));

        List<WebElement> list1 = OneMoreWebDriver.getInstance().findElements(
                By.cssSelector(objectLocators));
        listOfElements = list1;
        return list1;
    }

    /**
     * Find Element By ID
     */
    public void findElementById(String objectLocators) {

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        List<WebElement> list1 = wait.until(ExpectedConditions
                .presenceOfAllElementsLocatedBy(By.id(objectLocators)));

        listOfElements = list1;

    }

    /**
     * Find Element By Xpath
     */
    public void findElementByXpath(String objectLocators) {

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));

        wait.until(ExpectedConditions.presenceOfAllElementsLocatedBy(By
                .xpath(objectLocators)));

        List<WebElement> list1 = wait

                .until(ExpectedConditions.visibilityOfAllElements(OneMoreWebDriver
                        .getDriver().findElements(By.xpath(objectLocators))));

        listOfElements = list1;

    }

    /**
     * Find Element By Name
     */
    public void findElementByName(String objectLocators) {

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        wait.until(ExpectedConditions.visibilityOfAllElements(OneMoreWebDriver
                .getDriver().findElements(By.name(objectLocators))));

        List<WebElement> list1 = OneMoreWebDriver.getInstance().findElements(
                By.name(objectLocators));
        listOfElements = list1;

    }

    /**
     * Find corresponding method name in existing methods
     */
    public static Method findMethods(String methodName, Method[] methods) {

        for (int i = 0; i < methods.length; i++) {
            if (methodName.equalsIgnoreCase(methods[i].getName().toString())) {
                return methods[i];
            }
        }
        return null;
    }

    /**
     * Click on button/checkbox/radio button
     */
    public void click() {

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        wait.until(
                ExpectedConditions.elementToBeClickable(listOfElements.get(0))).click();
    }

    /**
     * Click on Submit button
     */
    public void submit() {
        listOfElements.get(0).submit();
    }

    /**
     * Enter data into text field/text area
     */
    public void enterText(String data) {
        listOfElements.get(0).sendKeys(data);
    }

    /**
     * Read the value present in the text field
     */
    public void readTextFieldValue() {
        listOfElements.get(0).getAttribute("value");
    }

    /**
     * Alert accept meaning click on OK button
     */
    public void alertAccept() {

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        wait.until(ExpectedConditions.alertIsPresent());

        wait1(2000);

        Alert alert = OneMoreWebDriver.getInstance().switchTo().alert();
        wait1(2000);

        alert.accept();
    }

    /**
     * Alert dismiss meaning click on Cancel button
     */
    public void alertDismiss() {
        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        wait.until(ExpectedConditions.alertIsPresent());
        wait1(2000);
        listOfElements.get(0).click();
        Alert alert = OneMoreWebDriver.getInstance().switchTo().alert();
        wait1(2000);
        alert.dismiss();
    }

    /**
     * Get the title of the page and verify the title
     */
    public void verifyTitleOfPage(String expectedTitle) {
        wait1(2000);
        String actual = OneMoreWebDriver.getInstance().getTitle().toString();
        actual.equalsIgnoreCase(expectedTitle);

    }

    /**
     * Make the driver to wait for specified amount of time
     */
    public void wait1(long i) {
        try {
            Thread.sleep(i);
        } catch (InterruptedException e) {
            System.out.println("InvalidFormatException" + e);
        }
    }

    /**
     * Select from the drop down list,if the drop down element tag is "SELECT" then use this method
     */
    public void selectDropDownByVisibleText(String textToSelect) {
        wait1(2000);

        WebDriverWait wait = new WebDriverWait(OneMoreWebDriver.getDriver(), Duration.ofSeconds(30));
        wait.pollingEvery(Duration.ofSeconds(2)).until(
                ExpectedConditions.elementToBeClickable(listOfElements.get(
                        0)));
        Select sel = new Select(listOfElements.get(0));
        sel.selectByVisibleText(textToSelect);
        wait1(2000);
    }

    /**
     * Select the value from a dropdown list by its index
     */
    public void selectDropDownByIndex(String parseIndex) {
        Select sel = new Select(listOfElements.get(0));
        sel.selectByIndex(Integer.parseInt(parseIndex));
    }

    /**
     * Select the value from a dropdown list by its value
     */
    public void selectDropDownByValue(String selectByValue) {
        Select sel = new Select(listOfElements.get(0));
        sel.selectByValue(selectByValue);
    }

    /**
     * Switch To frame( html inside another html)
     */
    public void switchToFrame() {
        OneMoreWebDriver.getInstance().switchTo()
                .frame(listOfElements.get(0));

    }

    /**
     * Switch back to previous frame or html
     */
    public void switchOutOfFrame() {
        OneMoreWebDriver.getInstance().switchTo().defaultContent();

    }

    /**
     * Select the multiple value from a dropdown list
     */
    public void selectFromListDropDown(String textValue) {
        wait1(2000);
        for (WebElement element1 : listOfElements) {

            if (element1.getText().equals(textValue)) {
                element1.click();
                break;
            }
        }

        wait1(2000);
    }

    public void selectFromAutoComplete(String textValue) {
        wait1(1000);
        enterText(textValue);
        // located element with contains()
        List<WebElement> m = findElementByTextContent(textValue);
        click();
    }


    /**
     * Navigate to next page
     */
    public void moveToNextPage() {
        OneMoreWebDriver.getInstance().navigate().forward();
    }

    /**
     * Navigate to previous page
     */
    public void moveToPreviousPage() {
        OneMoreWebDriver.getInstance().navigate().back();
    }

    /**
     * Maximize the window
     */
    public void maximizeWindow() {
        OneMoreWebDriver.getInstance().manage().window().maximize();
    }

    /**
     * Reads the text present in the web element
     */
    public void readText() {
        listOfElements.get(0).getText();
    }

    /**
     * Quit the application
     */
    public void quit() {
        OneMoreWebDriver.getInstance().quit();
    }

    /**
     * Closes the driver
     */
    public void close() {
        OneMoreWebDriver.getInstance().close();
    }

    /**
     * Checks that the element is displayed in the current web page
     */
    public void isDisplayed() {
        listOfElements.get(0).isDisplayed();
    }

    /**
     * Checks that the element is enabled in the current web page
     */
    public void isEnabled() {
        listOfElements.get(0).isEnabled();
    }

    /**
     * Selects a radio button
     */
    public void selectRadioButton() {
        listOfElements.get(0).click();
    }

    /**
     * Refresh the current web page
     */
    public void refreshPage() {
        OneMoreWebDriver.getInstance().navigate().refresh();
    }

    /**
     * Switch back to the parent window
     */
    public void switchToParentWindow() {
        String parentWindow = OneMoreWebDriver.getInstance().getWindowHandle();
        OneMoreWebDriver.getInstance().switchTo().window(parentWindow);
    }

    /**
     * Switche to the child window
     */
    public void switchToChildWindow(String title) {

        listOfElements.get(0).click();

        String parent = OneMoreWebDriver.getInstance().getWindowHandle();
        Set<String> windows = OneMoreWebDriver.getInstance().getWindowHandles();

        try {
            if (windows.size() > 1) {
                for (String child : windows) {
                    if (!child.equals(parent)) {

                        if (OneMoreWebDriver.getInstance().switchTo()
                                .window(child).getTitle()
                                .equals(title)) {

                            OneMoreWebDriver.getInstance().switchTo()
                                    .window(child);
                        }

                    }
                }
            }
        } catch (Exception e) {

            throw new RuntimeException("Exception", e);
        }

    }

    /**
     * Scrolls down the page till the element is visible
     */
    public void scrollElementIntoView() {
        wait1(1000);
        ((JavascriptExecutor) OneMoreWebDriver.getDriver())
                .executeScript("arguments[0].scrollIntoView(true);", listOfElements.get(0));
        wait1(1000);

    }

    /**
     * Scrolls down the page till the element is visible and clicks on the
     * element
     */
    public void scrollElementIntoViewClick() {
        Actions action = new Actions(OneMoreWebDriver.getDriver());
        action.moveToElement(listOfElements.get(0)).click().perform();
    }

    /**
     * Reads the url of current web page
     */
    public void readUrlOfPage() {
        OneMoreWebDriver.getInstance().getCurrentUrl();
    }


    /**
     * Navigates to the specified url
     */
    public void navigateToURL(String url) {
        OneMoreWebDriver.getInstance().navigate().to(url);
    }

    public static WebElement waitForElement(By by) {
        int count = 0;
        WebDriverWait wait = null;
        while (!(wait.until(ExpectedConditions.presenceOfElementLocated(by))
                .isDisplayed())) {
            wait = new WebDriverWait(OneMoreWebDriver.getInstance(), Duration.ofSeconds(60));
            wait.pollingEvery(Duration.ofSeconds(5));
            wait.until(ExpectedConditions.visibilityOfElementLocated(by))
                    .isDisplayed();
            wait.until(ExpectedConditions.presenceOfElementLocated(by))
                    .isDisplayed();
            count++;
            if (count == 100) {
                break;
            }
            return wait.until(ExpectedConditions.presenceOfElementLocated(by));
        }
        return wait.until(ExpectedConditions.presenceOfElementLocated(by));
    }

    /**
     * Provide Login name for window authentication
     */
    public static void windowAuthenticationLoginName(String data) {

        Alert alert = OneMoreWebDriver.getDriver().switchTo().alert();
        alert.sendKeys(data);
    }


    /**
     * verifies the data present in the text field
     */
    public boolean verifyTextFieldData(String data) {
        return listOfElements.get(0).getAttribute("value").equalsIgnoreCase(
                data);
    }


    /**
     * Verifies the Text present in the element
     */
    public boolean verifyText(String data) {

        return data.equalsIgnoreCase(listOfElements.get(0)
                .getText().toString());
    }


    /**
     * Selects the Date
     */
    public void selectDate(String date) {
        WebElement datePicker = OneMoreWebDriver.getDriver().findElement(
                By.id("ui-datepicker-div"));
        List<WebElement> noOfColumns = datePicker
                .findElements(By.tagName("td"));

        // Loop will rotate till expected date not found.
        for (WebElement cell : noOfColumns) {
            // Select the date from date picker when condition match.
            if (cell.getText().equals(date)) {
                cell.findElement(By.linkText(date)).click();
                break;
            }
        }

    }

    /**
     * Double clicks on the particular element
     */
    public void doubleClick() {
        Actions action = new Actions(OneMoreWebDriver.getDriver());
        action.doubleClick((WebElement) listOfElements).perform();

    }

    /**
     * Mouse hovering on the element is performed
     */
    public void singleMouseHover() {
        Actions action = new Actions(OneMoreWebDriver.getDriver());
        action.moveToElement((WebElement) listOfElements).perform();

    }

    /**
     * Right clicks on the element
     */
    public void rightClick() {
        Actions action = new Actions(OneMoreWebDriver.getDriver());
        action.contextClick((WebElement) listOfElements).perform();

    }

    /**
     * Select the check boxes
     */
    public void selectCheckBox() {
        boolean res = true;

        while (!listOfElements.get(0).isSelected()) {
            listOfElements.get(0).click();
            if (listOfElements.get(0).isSelected()) {
                res = false;
                break;
            }

        }

    }

    /**
     * Un-check the check box
     */
    public void deselectCheckBox() {
        boolean res = true;

        while (listOfElements.get(0).isSelected()) {
            listOfElements.get(0).click();
            if (!listOfElements.get(0).isSelected()) {
                res = false;
                break;
            }

        }

    }

    /**
     * Un-check the all check boxes
     */
    public void deselectAllCheckbox() {
        List<WebElement> list = listOfElements;

        for (WebElement element : list) {
            if (element.isSelected()) {
                element.click();
            }
        }
    }

    /**
     * Selects all the check boxes
     */
    public void selectAllCheckbox() {
        List<WebElement> list = listOfElements;

        for (WebElement element : list) {
            if (!element.isSelected()) {
                element.click();
            }
        }
    }

    /**
     * Verifies that the particular check box is selected
     */
    public boolean verifyCheckBoxSelected() {

        return (listOfElements.get(0).isSelected());

    }

}
