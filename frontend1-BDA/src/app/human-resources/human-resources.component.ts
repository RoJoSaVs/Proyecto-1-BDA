//dynamic components loading:https://www.c-sharpcorner.com/article/how-to-create-dynamic-components-in-angular-application/

import {  
  Component,  
  OnInit,
  ComponentFactoryResolver,  
  ViewChild,  
  ElementRef,  
  ViewContainerRef,  
} from '@angular/core';  

import { AplicantesITComponent } from '../aplicantes-it/aplicantes-it.component'
import { AplicantesInglesComponent } from '../aplicantes-ingles/aplicantes-ingles.component'
import { AplicantesNoITComponent } from '../aplicantes-no-it/aplicantes-no-it.component'

interface Opciones {
  value: string;
}

@Component({
  selector: 'app-human-resources',
  templateUrl: './human-resources.component.html',
  styleUrls: ['./human-resources.component.css']
})
export class HumanResourcesComponent implements OnInit {
  //instructions to load components dynamically
  @ViewChild('container', { read: ViewContainerRef })  
  container!: ViewContainerRef;  
  
  constructor(private componentFactoryResolver: ComponentFactoryResolver) 
  //select variables
  { this.selectedOption = "",
  this.selectedOption = ""} 


  //select options

  selectedOption: string;
  options = [
    { name: "Aplicantes de IT", value: "Aplicantes de IT" },
    { name: "Aplicantes de inglés avanzado", value: "Aplicantes de inglés avanzado" },
    { name: "Aplicantes fuera del área de IT", value: "Aplicantes fuera del área de IT" }
  ]

  // asign components 
  aplicantesIT = this.componentFactoryResolver.resolveComponentFactory(AplicantesITComponent);  
  aplicantesNoIT = this.componentFactoryResolver.resolveComponentFactory(AplicantesNoITComponent);
  aplicantesIngles = this.componentFactoryResolver.resolveComponentFactory(AplicantesInglesComponent);


  ngOnInit(): void {
     
  }

  onSubmit() {
    //clear previous components (if exists)
    this.container.clear();

  
    // add the component to the view  

    if(this.selectedOption =="Aplicantes de IT"){
      const componentRef = this.container.createComponent(this.aplicantesIT); 
    }
    if(this.selectedOption =="Aplicantes de inglés avanzado"){
      const componentRef = this.container.createComponent(this.aplicantesIngles); 
    }

    if(this.selectedOption =="Aplicantes fuera del área de IT"){
      const componentRef = this.container.createComponent(this.aplicantesNoIT); 
    }



    
    //alert(this.selectedOption);
  }

}
