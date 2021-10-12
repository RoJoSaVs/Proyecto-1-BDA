import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ApplicantComponent } from './applicant/applicant.component';
import { HumanResourcesComponent } from './human-resources/human-resources.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import {Router, RouterModule, Routes} from "@angular/router";
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

const appRoutes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent},
  { path: 'hr', component: HumanResourcesComponent},
  { path: 'applicant', component: ApplicantComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    ApplicantComponent,
    HumanResourcesComponent,
    LoginComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    FormsModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
