package com.testbud.onemore.model;


import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class OneMoreCommonResponse {
    private String message;
    private List<String> error;
}
