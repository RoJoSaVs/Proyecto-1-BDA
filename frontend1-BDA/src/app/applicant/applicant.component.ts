import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
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

  ngOnInit(): void {
    this.email = this.service.email;
    /*
    this.router.params.subscribe(event => {
      this.email = event.id;
    });
    */
  }
}
