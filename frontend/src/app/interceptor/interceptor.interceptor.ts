import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { ServiceService } from '../service/service.service';
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse } from '@angular/common/http';
import { catchError, switchMap, throwError } from 'rxjs';

export const interceptorInterceptor: HttpInterceptorFn = (req, next) => {
  const authService = inject(ServiceService);
  const http = inject(HttpClient);

  const access = authService.getAccessToken();



  let authReq = req;

  if (access) {
    authReq = req.clone({
      setHeaders: {
        Authorization: `Bearer ${access}`,
      },
    });
  }

  return next(authReq).pipe(
    catchError((err: HttpErrorResponse) => {
      if (err.status === 401 && authService.getRefreshToken()) {
        return authService.updateAccessToken(authService.getRefreshToken()!).pipe(
          switchMap((res) => {
            authService.saveTokens(res.access, res.refresh);
        
            const newReq = req.clone({
              setHeaders: {
                Authorization: `Bearer ${res.access}`,
              },
            });
            return next(newReq);
          }),
          catchError(() => {
            authService.logout();
            return throwError(() => new Error('Unauthorized'));
          })
        );
      }

      return throwError(() => err);
    })
  );
};
