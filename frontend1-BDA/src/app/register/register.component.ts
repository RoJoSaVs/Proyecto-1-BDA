import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  private lenguages: string[];
  private titles: string[];
  private programmingSkills: string[];

  constructor(private router: Router) {
    this.lenguages = [];
    this.titles = [];
    this.programmingSkills = [];
  }

  ngOnInit(): void {
  }

  onRegister(): void {

    this.router.navigate(['applicant'])
  }
}
