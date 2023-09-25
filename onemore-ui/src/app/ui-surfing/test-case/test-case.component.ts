import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AppCommonComponent } from 'src/app/core/app-common-component';

@Component({
  selector: 'app-test-case',
  templateUrl: './test-case.component.html',
  styleUrls: ['./test-case.component.scss'],
})
export class TestCaseComponent extends AppCommonComponent implements OnInit {
  @Input()
  testcase: any;


  formGroup: FormGroup = new FormGroup({
    id: new FormControl(''),
    test_suite: new FormControl(''),
    testcase_name: new FormControl(''),
    test_case_type: new FormControl(''),
    test_case_details: new FormGroup({
      selector_group: new FormGroup({
        css_selector: new FormGroup({
          is_selected: new FormControl(false),
          selector: new FormControl(''),
        }),
        id_selector: new FormGroup({
          is_selected: new FormControl(false),
          selector: new FormControl(''),
        }),
        xpath_selector: new FormGroup({
          is_selected: new FormControl(false),
          selector: new FormControl(''),
        }),
      }),
      action: new FormGroup({
        eneter_value: new FormGroup({
          value: new FormControl(''),
        }),
      }),
    }),
  });

  ngOnInit(): void {
    this.formGroup.patchValue(this.testcase);
  }

  saveTestCase() {
    this.http
      .post(
        this.appStoreService.getAipUrl(this.API_UPDATE_TEST_CASE),
        this.formGroup.getRawValue()
      )
      .subscribe(
        (response: any) => {
          this.notificationService.sendMessage({
            message: 'Saved Test case !',
            type: 0,
          });
          this.appStoreService.REFRESH_TS.next(this.formGroup.getRawValue());
        },
        (error) => {
          this.handleError(error);
        }
      );
  }
}
