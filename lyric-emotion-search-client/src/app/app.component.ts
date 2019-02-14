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
    this.results = [{
      author: 'author1',
      song_name: 'song1',
      happy_score: 0.25,
      sad_score: 0.25,
      relaxed_score: 0.25,
      angry_score: 0.25,
      lyrics: 'lyrics sample1'
    },
    {
      author: 'author2',
      song_name: 'song2',
      happy_score: 0.35,
      sad_score: 0.15,
      relaxed_score: 0.35,
      angry_score: 0.15,
      lyrics: 'lyrics sample2'
    }];
  }

  search() {
    const url = "http:\\\\localhost:5000\\api\\search";
    return this.http.post<Array<SearchResult>>(url, this.filter)
      .subscribe(res => {
        this.results = res;
      }, error => {
        console.log(error);
      });
  }
}

class Filter {
  term: string;
  category: string;
}

class SearchResult {
  author: string;
  song_name: string;
  happy_score: number;
  sad_score: number;
  relaxed_score: number;
  angry_score: number;
  lyrics: string;
}