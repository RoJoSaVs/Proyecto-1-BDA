import {Component, OnInit, ViewChild} from '@angular/core';
import {NgForm} from "@angular/forms";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
  /**
   * This class is in charge of holding the login form
   */
  export class LoginComponent implements OnInit {
  @ViewChild('login') loginForm: NgForm;

  constructor() { }

  ngOnInit(): void {
  }

  onLogin(): void {
    console.log(this.loginForm.value.username);
  }
}

