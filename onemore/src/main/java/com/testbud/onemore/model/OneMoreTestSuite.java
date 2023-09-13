package com.testbud.onemore.model;

import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class OneMoreTestSuite {

    private String testSuiteName;
    private String testSuiteDesc;
    private List<OneMoreUiTestCase> mascotaTestCaseList;

}
