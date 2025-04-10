import { Component } from '@angular/core';
import { Company } from '../../interfaces/company';
import { ServiceService } from '../../service/service.service';
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-companylist',
  imports: [NgFor, FormsModule],
  templateUrl: './companylist.component.html',
  styleUrl: './companylist.component.css'
})
export class CompanylistComponent {
  companies: Company[] = []
  constructor(private service: ServiceService){

  }

  ngOnInit(): void {
    this.service.getCompanies().subscribe(
      {
        next: (data) => this.companies = data,
        error: (err) => console.error('Ошибка при получении компании' , err)
      }
    )
  }
}
