import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TestCaseComponent } from './test-case.component';

describe('TestCaseComponent', () => {
  let component: TestCaseComponent;
  let fixture: ComponentFixture<TestCaseComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TestCaseComponent]
    });
    fixture = TestBed.createComponent(TestCaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
