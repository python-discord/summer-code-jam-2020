import {Comment} from './comment';

export interface CommentsContext {
  count: number;
  next: string;
  previous: string;
  results: Comment[];
}
