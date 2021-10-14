import {Component, OnInit, ViewChild} from '@angular/core';
import {Router} from "@angular/router";
import {NgForm} from "@angular/forms";
import {ConnectionService} from "../services/connection.service";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  @ViewChild('register') registerForm: NgForm;

  constructor(private router: Router, private service: ConnectionService) {
  }

  ngOnInit(): void {
  }

  onRegister(): void {
    console.log(this.registerForm);
    this.service.Post(this.registerForm.value,'https://proyecto-1-bda.rojosavs.repl.co/api/add_employee').subscribe(
      res=>{
        console.log(res)
        if (res === 0) {
          this.router.navigate(['login']);
        }
      }
    );
  }
}
