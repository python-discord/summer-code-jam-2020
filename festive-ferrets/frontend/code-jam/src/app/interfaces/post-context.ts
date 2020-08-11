import {Post} from './post';

export interface PostContext {
  count:number;
  next:string;
  previous:string;
  results:Post[];
}
