import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ConnectionService } from '../services/connection.service';
import { Aplicantes } from '../services/aplicantes.model';

@Component({
  selector: 'app-aplicantes-ingles',
  templateUrl: './aplicantes-ingles.component.html',
  styleUrls: ['./aplicantes-ingles.component.css']
})
export class AplicantesInglesComponent implements OnInit {

  constructor(private httpClient: HttpClient,
    private service : ConnectionService) { }

  readonly rootURL = 'https://proyecto-1-bda.rojosavs.repl.co/api/query1';

  aplicantes: Aplicantes[] ;

  ngOnInit(): void {
    this.httpClient.get<any>(this.rootURL).subscribe(
      response => {
          this.aplicantes = response;
      },
    );
  }

  

}
