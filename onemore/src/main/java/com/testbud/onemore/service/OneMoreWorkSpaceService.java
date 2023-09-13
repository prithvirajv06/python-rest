package com.testbud.onemore.service;


import com.testbud.onemore.model.OneMoreCommonResponse;
import com.testbud.onemore.model.OneMoreTestSuite;
import com.testbud.onemore.model.OneMoreUiWorkSpace;

import java.util.List;

public interface OneMoreWorkSpaceService {

    public OneMoreUiWorkSpace createMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace);

    public List<OneMoreUiWorkSpace> getMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace);

    public OneMoreUiWorkSpace updateMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace);

    public void deleteMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace);

    public OneMoreCommonResponse runTestSuite(OneMoreTestSuite oneMoreTestSuite);

}
