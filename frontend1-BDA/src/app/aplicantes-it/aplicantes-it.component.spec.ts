import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AplicantesITComponent } from './aplicantes-it.component';

describe('AplicantesITComponent', () => {
  let component: AplicantesITComponent;
  let fixture: ComponentFixture<AplicantesITComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AplicantesITComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AplicantesITComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
