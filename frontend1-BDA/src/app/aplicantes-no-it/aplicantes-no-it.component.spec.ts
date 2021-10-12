import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AplicantesNoITComponent } from './aplicantes-no-it.component';

describe('AplicantesNoITComponent', () => {
  let component: AplicantesNoITComponent;
  let fixture: ComponentFixture<AplicantesNoITComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AplicantesNoITComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AplicantesNoITComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
