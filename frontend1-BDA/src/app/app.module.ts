import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HumanResourcesComponent } from './human-resources/human-resources.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import {RouterModule} from "@angular/router";
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AplicantesITComponent } from './aplicantes-it/aplicantes-it.component';
import { AplicantesInglesComponent } from './aplicantes-ingles/aplicantes-ingles.component';
import { AplicantesNoITComponent } from './aplicantes-no-it/aplicantes-no-it.component';

@NgModule({
  declarations: [
    AppComponent,
    HumanResourcesComponent,
    LoginComponent,
    RegisterComponent,
    AplicantesITComponent,
    AplicantesInglesComponent,
    AplicantesNoITComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    FormsModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
