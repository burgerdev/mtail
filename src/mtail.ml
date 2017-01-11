
(* Formats any string to a string of exactly `width` characters. TODO *)
let format_width width text =
  let n = String.length text in
  if n > width then
    Str.first_chars text width
  else
    text ^ String.make (width - n) ' '

(* Convert a re to a predicate that returns true iff the re matches. *)
let predicate_of_regexp re =
  let matcher x =
    try
      let _ = Str.search_forward re x 0 in true
    with
    | Not_found -> false in matcher

(* Create a list that alternates between the items of `l` and item `s`.  *)
let interleave_with s l =
  let rec aux l acc =
    match l with
    | h :: [] -> h :: acc
    | [] -> acc
    | h :: t -> aux t (s :: h :: acc)
  in List.rev (aux l [])

(* Takes a list of predicates and a string, and outputs a list of string
   options. *)
let columns_of_string list_of_predicates line =
  List.map (fun p -> if p line then Some line else None) list_of_predicates
