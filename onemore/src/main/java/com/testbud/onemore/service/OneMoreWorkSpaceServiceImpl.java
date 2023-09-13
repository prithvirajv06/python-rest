package com.testbud.onemore.service;
import com.testbud.onemore.model.OneMoreCommonResponse;
import com.testbud.onemore.model.OneMoreTestSuite;
import com.testbud.onemore.model.OneMoreUiWorkSpace;
import com.testbud.onemore.repository.OneMoreUiWorkSpaceRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class OneMoreWorkSpaceServiceImpl implements OneMoreWorkSpaceService {

    @Autowired
    OneMoreUiWorkSpaceRepo oneMoreUiWorkSpaceRepo;


    @Override
    public OneMoreUiWorkSpace createMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        return oneMoreUiWorkSpaceRepo.insert(oneMoreUiWorkSpace);
    }

    @Override
    public List<OneMoreUiWorkSpace> getMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        return oneMoreUiWorkSpaceRepo.findAll();
    }

    @Override
    public OneMoreUiWorkSpace updateMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        return oneMoreUiWorkSpaceRepo.save(oneMoreUiWorkSpace);
    }

    @Override
    public void deleteMtcUiWorkSpace(OneMoreUiWorkSpace oneMoreUiWorkSpace) {
        oneMoreUiWorkSpaceRepo.deleteById(oneMoreUiWorkSpace.getId());
    }

    @Override
    public OneMoreCommonResponse runTestSuite(OneMoreTestSuite oneMoreTestSuite) {
        return null;
    }
}
