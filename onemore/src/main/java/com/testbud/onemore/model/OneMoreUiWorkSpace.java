package com.testbud.onemore.model;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document("mct_interface_workspace")
public class OneMoreUiWorkSpace {
    @org.springframework.data.annotation.Id
    private String Id;
    private String workspaceName;
    private String workSpaceDesc;
    private List<String> mascotaTestSuiteList;
}
