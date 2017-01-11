
open Mtail
open Cmdliner

let bin_name = "mtail"
let bin_version = "1.0-a"

let main width patterns =
  let regexps = List.map Str.regexp patterns in
  let predicates = List.map predicate_of_regexp regexps in

  let handle line =
    (*let line = String.trim line in*)
    let cols = columns_of_string predicates line in
    let mapper = function
      | Some s -> format_width width s
      | None -> String.make width ' ' in
    let out_strings = List.map mapper cols in
    List.iter print_string (interleave_with "|" out_strings);
    print_endline "" in

  let produce_line _ =
    try
      Some (input_line stdin)
    with
    | End_of_file -> None in

  Stream.iter handle (Stream.from produce_line)

(* Cmdliner stuff *)

let width_term =
  let doc = "Width of one column." in
  Arg.(value & opt int 20 & info ["w"; "width"] ~docv:"WIDTH" ~doc)

let patterns_term = Arg.(non_empty & pos_all string [] & info [] ~docv:"REGEXP")

let main_term = Term.(const main $ width_term $ patterns_term)

let info =
  let doc = "Format input into columns according to regular expressions." in
  Term.info bin_name ~version:bin_version ~doc

let () = match Term.eval (main_term, info) with `Error _ -> exit 1 | _ -> exit 0
