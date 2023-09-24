import {
  HttpHandler,
  HttpInterceptor,
  HttpRequest,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppStoreService } from '../app-store.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor() {}

  intercept(req: HttpRequest<any>, next: HttpHandler) {
    // Get the auth token from the service.
    const authToken = localStorage.getItem('one_token');

    // Clone the request and replace the original headers with
    // cloned headers, updated with the authorization.
    const authReq = req.clone({
      headers: req.headers.set('Authorization', 'Bearer ' + authToken),
    });

    // send cloned request with header to the next handler.
    return next.handle(authReq);
  }
}
