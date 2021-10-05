import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ConnectionService } from '../services/connection.service';
import { Aplicantes } from '../services/aplicantes.model';

@Component({
  selector: 'app-aplicantes-no-it',
  templateUrl: './aplicantes-no-it.component.html',
  styleUrls: ['./aplicantes-no-it.component.css']
})
export class AplicantesNoITComponent implements OnInit {


  constructor(private httpClient: HttpClient,
    private service : ConnectionService) { }

  readonly rootURL = 'https://proyecto-1-bda.rojosavs.repl.co/api/query3';

  aplicantes: Aplicantes[] ;

  ngOnInit(): void {
    this.httpClient.get<any>(this.rootURL).subscribe(
      response => {
          this.aplicantes = response;
      },
    );
  }

}
