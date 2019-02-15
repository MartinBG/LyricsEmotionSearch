import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'lyric-emotion-search-client';

  filter = new Filter();
  results: Array<SearchResult> = [];

  constructor(private http: HttpClient) {
  }

  search() {
    const url = "http:\\\\127.0.0.1:5000\\api\\search";
    return this.http.post<Array<SearchResult>>(url, this.filter)
      .subscribe(res => {
        let new_res = this.normalize(res);
        console.log(new_res)
        new_res = this.sort(new_res);
        this.results = new_res;
      }, error => {
        console.log(error);
      });
  }

  normalize(arr: Array<SearchResult>): Array<SearchResult> {
    arr.forEach(element => {
      element.normalized_lyrics = element.lyrics.split('.');
      element['angry_score'] = element['angry_score']*100;
      element['happy_score'] = element['happy_score']*100;
      element['relaxed_score'] = element['relaxed_score']*100;
      element['sad_score'] = element['sad_score']*100;
    });
    return arr;
  }

  sort(arr: Array<SearchResult>): Array<SearchResult> {
    if(!this.filter.emotion)
      return arr;

    const emotion_term = this.filter.emotion + "_score";
    arr.sort((el1, el2) => { 
      if(el1[emotion_term] > el2[emotion_term])
        return -1;
    })
    return arr;
  }
}

class Filter {
  term: string;
  emotion: string;
}

class SearchResult {
  author: string;
  song_name: string;
  happy_score: number;
  sad_score: number;
  relaxed_score: number;
  angry_score: number;
  lyrics: string;
  normalized_lyrics: Array<string>;
  opened_lyrics: boolean;
}