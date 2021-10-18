import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import { Aplicante_info } from '../services/aplicante_info.model';
import {ConnectionService} from "../services/connection.service";

@Component({
  selector: 'app-applicant',
  templateUrl: './applicant.component.html',
  styleUrls: ['./applicant.component.css']
})
export class ApplicantComponent implements OnInit {
  public email: string;

  constructor(private router: ActivatedRoute, private service: ConnectionService) {
    this.email = this.service.email;
  }

  readonly rootURL = 'https://proyecto-1-bda.rojosavs.repl.co/api/single_employee?email='+this.service.email;

  aplicante_info: Aplicante_info;

  ngOnInit(): void {
    this.email = this.service.email;
    this.service.Get(this.rootURL).subscribe(
      response => {
          console.log(response);
          this.aplicante_info = response;
          console.log(this.aplicante_info);
          this.aplicante_info.languajes = JSON.stringify(this.aplicante_info.languajes)
          console.log(typeof(this.aplicante_info.languajes));
      }
    );

  }
}
