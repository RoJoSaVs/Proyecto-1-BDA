//desde este módulo se realizan todas las conexiones con el backend

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })

export class ConnectionService {
  currentUser: string;

  items = [];

  //utiliza la bilbioteca HttpClient de angular
  constructor(
    private http: HttpClient
  ) {}


  //postea hacia el server
  Post(val:any,postURL: string){
    return this.http.post<any>(postURL,val);
  }

  //permite actualizar un valor basado en una id
  Update(val:any,updateURL: string){
    return this.http.put<boolean>(updateURL,val);
  }

  //realiza un get a un URL
  Get(getURL: string){
    return this.http.get<any>(getURL);
  }

  //Realiza un delete hacia un URL
  Delete(val:any,deleteURL: string){
    return this.http.delete(deleteURL,val);
  }


}
