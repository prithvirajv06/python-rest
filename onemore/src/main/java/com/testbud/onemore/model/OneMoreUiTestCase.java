package com.testbud.onemore.model;


import lombok.*;


@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class OneMoreUiTestCase {

    private String id ;
    private String title;
    private String shortDesc;
    private Boolean isAssertionTestCase;
    private String objectLocator;
    private String objectLocatorType;
    private String actions;
    private String actionValue;
    private String interfaceAssertion;
    private OneMoreUiTestCase onTrueAssertion;
    private OneMoreUiTestCase onFalseAssertion;

}
