package com.testbud.onemore.repository;

import com.testbud.onemore.model.OneMoreUiWorkSpace;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface OneMoreUiWorkSpaceRepo extends MongoRepository<OneMoreUiWorkSpace, String> {
}
