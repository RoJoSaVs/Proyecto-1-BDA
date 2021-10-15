import {Component, OnInit, ViewChild} from '@angular/core';
import {NgForm} from "@angular/forms";
import {Router} from "@angular/router";
import {ConnectionService} from "../services/connection.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
  /**
   *
   */
  export class LoginComponent implements OnInit {
  @ViewChild('login') loginForm: NgForm;

  constructor(private router: Router, private service: ConnectionService) { }

  ngOnInit(): void {
  }

  // Lo que sucede cuando se hace un login
  onLogin(): void {
    console.log(this.loginForm.value);

    this.service.Post(this.loginForm.value,'https://proyecto-1-bda.rojosavs.repl.co/login').subscribe(
      res=>{
        console.log(res)
        if (res === 'admin') {
          this.router.navigate(['hr']);
        }
        if (res === 'Employee') {
          this.service.email = this.loginForm.value.email;
          // this.router.navigate(['applicant',this.loginForm.value.password]);
          this.router.navigate(['applicant']);
        }
      }
    );
  }

  onNoAccount(): void {
    this.router.navigate(['register']);
  }
}

