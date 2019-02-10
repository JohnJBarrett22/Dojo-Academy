import { Component } from '@angular/core';
import { HttpService } from './http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Heroes';
  heroes = [];
  hero = {};
  private _httpService: HttpService;

  constructor(_httpService: HttpService) {
    this._httpService = _httpService;
  }

  ngOnInit(){
    let observable = this._httpService.getAll();
    observable.subscribe( data => {
      this.heroes = data['heroes']
    });
  }

  newHero(){
    let observable = this._httpService.create(this.hero);
    observable.subscribe( data => {
      console.log(data);
      this.hero = {};
      this.ngOnInit();
    });
  }

  imageAdded(e){
    console.log("someone added an image", e);
    let _this = this;        
    let file = e.target.files[0];        
    let reader = new FileReader();        
    reader.addEventListener("load", function() {                
        _this.hero['filename'] = file.name;                
        _this.hero['image'] = reader.result;    
        console.log(_this.hero);                  
    }, false);
    if (file) {              
        reader.readAsDataURL(file);        
    }
  }
}