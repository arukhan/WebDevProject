import { Component } from '@angular/core';
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Resume } from '../../interfaces/resume';
import { ServiceService } from '../../service/service.service';
@Component({
  selector: 'app-resumelist',
  imports: [NgFor, NgIf, FormsModule],
  templateUrl: './resumelist.component.html',
  styleUrl: './resumelist.component.css'
})
export class ResumelistComponent {
  resumes: Resume[] = []
  constructor(private ser:ServiceService){
  
  }
  
    ngOnInit(): void {
      this.ser.getResume().subscribe(
        {
          next: (data) => this.resumes = data,
          error: (err) => console.error('Ошибка при получении резюме' , err)
        }
      );
    }

}
