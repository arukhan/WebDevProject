import { Routes } from '@angular/router';
import { LoginComponent } from './login/login/login.component';
import { RegisterComponent } from './register/register/register.component';
import { CompanylistComponent } from './companylist/companylist/companylist.component';
import { VacancylistComponent } from './vacancylist/vacancylist/vacancylist.component';
import { ProtectedComponent } from './protected/protected/protected.component';
import { ResumelistComponent } from './resumelist/resumelist/resumelist.component';
export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    { path: 'company', component: CompanylistComponent },
    { path: 'vacancy', component: VacancylistComponent },
    { path: 'protected', component: ProtectedComponent },
    { path: 'resume', component: ResumelistComponent },
    { path: '', component: RegisterComponent },
  ];
