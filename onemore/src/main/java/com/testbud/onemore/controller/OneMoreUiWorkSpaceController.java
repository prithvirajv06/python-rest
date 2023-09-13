package com.testbud.onemore.controller;
import com.testbud.onemore.model.OneMoreUiWorkSpace;
import com.testbud.onemore.service.OneMoreWorkSpaceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping(path = "/ui-testing/workspace")
public class OneMoreUiWorkSpaceController {

    @Autowired
    OneMoreWorkSpaceService oneMoreWorkSpaceService;



    @PostMapping("/create")
    public OneMoreUiWorkSpace createWorkSpace(@RequestBody OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        return oneMoreWorkSpaceService.createMtcUiWorkSpace(oneMoreUiWorkSpace);
    }

    @PostMapping("/get-my-workspace")
    public List<OneMoreUiWorkSpace> getWorkSpace(@RequestBody OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        return oneMoreWorkSpaceService.getMtcUiWorkSpace(oneMoreUiWorkSpace);
    }

    @PostMapping("/update")
    public OneMoreUiWorkSpace updateMtcUiWorkSpace(@RequestBody OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        return oneMoreWorkSpaceService.updateMtcUiWorkSpace(oneMoreUiWorkSpace);
    }

    @PostMapping("/delete")
    public void deleteMtcWorkspace(@RequestBody OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        oneMoreWorkSpaceService.deleteMtcUiWorkSpace(oneMoreUiWorkSpace);
    }


}
