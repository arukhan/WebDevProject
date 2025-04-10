import { Component } from '@angular/core';
import { Vacancy } from '../../interfaces/vacancy';
import { OnInit } from '@angular/core';
import { ServiceService } from '../../service/service.service';
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-vacancylist',
  imports: [NgFor, NgIf, FormsModule],
  templateUrl: './vacancylist.component.html',
  styleUrl: './vacancylist.component.css'
})
export class VacancylistComponent implements OnInit{
  vacancies: Vacancy[] = [];

  constructor(private ser:ServiceService){

  }

  ngOnInit(): void {
    this.ser.getVacancies().subscribe(
      {
        next: (data) => this.vacancies = data,
        error: (err) => console.error('Ошибка при получении вакансии' , err)
      }
    );
  }



}

