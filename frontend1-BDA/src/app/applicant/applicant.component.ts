import {Component, OnInit, ViewChild} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import { Aplicante_info } from '../services/aplicante_info.model';
import {ConnectionService} from "../services/connection.service";
import {NgForm} from "@angular/forms";

@Component({
  selector: 'app-applicant',
  templateUrl: './applicant.component.html',
  styleUrls: ['./applicant.component.css']
})
export class ApplicantComponent implements OnInit {
  @ViewChild('update') updateForm: NgForm;
  public email: string;
  aplicante_info: Aplicante_info;
  readonly rootURL = 'https://proyecto-1-bda.rojosavs.repl.co/api/single_employee?email='+this.service.email;
  readonly updateURL = 'https://proyecto-1-bda.rojosavs.repl.co/api/edit_employee?email='+this.service.email;

  constructor(private router: ActivatedRoute, private service: ConnectionService) {
    this.email = this.service.email;
  }

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

  onUpdate(): void {
    this.updateForm.value.languajes=JSON.parse("{"+this.updateForm.value.languajes+"}");
    this.updateForm.value.university_degree=this.updateForm.value.university_degree.split(",");
    this.updateForm.value.programming_languages=this.updateForm.value.programming_languages.split(",");
    console.log(this.updateForm.value);
    this.service.Update(this.updateForm.value,this.updateURL).subscribe(
      res=>{
        console.log(res)
        if (res === true) {
          console.log('Exito');
        }
      }
    );
  }
}
