open OUnit
open Mtail

let empty_list = []
let list_a = [1;2;3]

let test_predicate_of_regexp _ =
  let re = Str.regexp "asdf" in
  assert (predicate_of_regexp re "asdf");
  assert (predicate_of_regexp re "ghasdfjk");
  assert (not (predicate_of_regexp re "ghjk"))

let test_format_width _ =
  let long = "asdf" in
  let expected_truncated = "as" in
  let short = "a" in
  let expected_padded = "a " in
  assert_equal expected_padded (format_width 2 short);
  assert_equal expected_truncated (format_width 2 long);
  assert_equal expected_truncated (format_width 2 expected_truncated)

let test_interleave_with _ =
  let l = [1; 2; 3] in
  let i = 0 in
  let expected = [1; 0; 2; 0; 3] in
  assert_equal expected (interleave_with i l)

let suite =
  "mtail suite" >::: ["test_predicate_of_regexp" >:: test_predicate_of_regexp;
                      "test_format_width" >:: test_format_width;
                      "test_interleave_with" >:: test_interleave_with]

let _ =
  run_test_tt_main suite
