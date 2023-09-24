import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AppCommonComponent } from 'src/app/core/app-common-component';
import { env } from 'src/environment';

@Component({
  selector: 'app-test-suite',
  templateUrl: './test-suite.component.html',
  styleUrls: ['./test-suite.component.scss'],
})
export class TestSuiteComponent extends AppCommonComponent implements OnInit {
  testsuiteList: [any] = [{}];
  isCreate = true;
  modeOfScreen = 'ENQ';
  // modeOfScreen = 'TES_EDIT';
  selectedTestSuite: any = {};
  formGroup: FormGroup = new FormGroup({
    id: new FormControl(''),
    user: new FormControl(''),
    workspace: new FormControl(''),
    testsuite_name: new FormControl('', [Validators.required]),
    description: new FormControl('', [Validators.required]),
    application: new FormControl('', [Validators.required]),
    locaderCss: new FormControl('', [Validators.required]),
  });
  workspaceID: any;
  testCaseList: any;
  showTestCase: boolean = false;
  selectedTestCase: any;

  ngOnInit(): void {
    this.workspaceID = this.appStoreService.getCommonVar(this.CONST_WS_ID);
    this.getAllTestSuite();
    this.appStoreService.REFRESH_TS.subscribe((data) => {
      this.setTestCaseData();
    });
  }

  createTS() {
    this.modeOfScreen = 'CREATE';
    this.formGroup.reset();
    this.formGroup.patchValue({
      workspace: this.workspaceID,
    });
  }

  getAllTestSuite() {
    this.http
      .post(this.appStoreService.getAipUrl(this.API_GET_ALL_TEST_SUITE), {
        workspace: this.workspaceID,
      })
      .subscribe(
        (response: any) => {
          this.testsuiteList = response.data;
        },
        (error) => {
          this.testsuiteList.pop();
          this.handleError(error);
        }
      );
  }

  goToWorkspace() {
    this.route.navigateByUrl(this.ROUTE_UI_WORKSPACE);
  }

  saveTestsuite() {
    this.http
      .post(
        this.appStoreService.getAipUrl(this.API_SAVE_TEST_SUITE),
        this.formGroup.getRawValue()
      )
      .subscribe(
        (response: any) => {
          this.modeOfScreen = 'ENQ';
          this.getAllTestSuite();
        },
        (error) => {
          this.testsuiteList.pop();
          this.handleError(error);
        }
      );
  }

  deleteTestSuite(testSuiteId: any) {
    this.http
      .post(this.appStoreService.getAipUrl(this.API_DELETE_TEST_SUITE), {
        id: testSuiteId,
      })
      .subscribe(
        (response: any) => {
          this.notificationService.sendMessage({
            message: 'Test suite deleted !',
            type: 0,
          });
          this.getAllTestSuite();
        },
        (error) => {
          this.testsuiteList.pop();
          this.handleError(error);
        }
      );
  }

  updateTestsuite() {}

  editTestSuite(ts: any) {
    this.modeOfScreen = 'TES_EDIT';
    this.selectedTestSuite = ts;
    this.getAllTestCase(ts);
  }

  getAllTestCase(ts: any) {
    this.http
      .post(this.appStoreService.getAipUrl(this.API_GET_ALL_TEST_CASE), {
        testsuite: ts.id,
      })
      .subscribe(
        (response: any) => {
          this.testCaseList = response.data;
        },
        (error) => {
          this.testsuiteList.pop();
          this.handleError(error);
        }
      );
  }

  /**Test Case Section */

  testCaseName = '';
  addNewTestCase() {
    this.showTestCase = true;
  }
  saveTestCase() {
    this.http
      .post(this.appStoreService.getAipUrl(this.API_SAVE_TEST_CASE), {
        testcase_name: this.testCaseName,
        test_suite: this.selectedTestSuite.id,
      })
      .subscribe(
        (response: any) => {
          this.testCaseList = response.data;
          this.testCaseName = '';
          this.showTestCase = false;
          this.getAllTestCase(this.selectedTestSuite);
        },
        (error) => {
          this.testsuiteList.pop();
          this.handleError(error);
        }
      );
  }

  deleteTestCase(tc: any) {
    this.http
      .post(this.appStoreService.getAipUrl(this.API_DELETE_TEST_CASE), {
        id: tc.id,
      })
      .subscribe(
        (response: any) => {
          this.notificationService.sendMessage({
            message: 'Test case deleted !',
            type: 0,
          });
          this.getAllTestCase(this.selectedTestSuite);
        },
        (error) => {
          this.testsuiteList.pop();
          this.handleError(error);
        }
      );
  }

  editTestCase(testcase: any) {
    this.selectedTestCase = null;
    this.http
      .post(this.appStoreService.getAipUrl(this.API_GET_TEST_CASE), testcase)
      .subscribe(
        (response: any) => {
          this.selectedTestCase = response.data;
        },
        (error) => {
          this.testsuiteList.pop();
          this.handleError(error);
        }
      );
  }

  setTestCaseData() {
    this.getAllTestCase(this.selectedTestSuite);
  }
}
