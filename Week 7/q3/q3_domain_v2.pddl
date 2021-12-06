(define (domain pacmanD)
    (:requirements :strips)
    (:types pacman loc)
    (:predicates (pacman-at ?p - pacman ?l - loc) (east ?l1 - loc ?l2 - loc) (west ?l1 - loc ?l2 - loc) (north ?l1 - loc ?l2 - loc) (south ?l1 - loc ?l2 - loc) (eaten ?l - loc) (dot-at ?l - loc)
    ) 
    
    (:action move-West
        :parameters (?p - pacman ?l1 - loc ?l2 - loc)
        :precondition (and (pacman-at ?p ?l1) (west ?l2 ?l1) (not (= ?l1 ?l2)))
        :effect (and (not (pacman-at ?p ?l1)) (pacman-at ?p ?l2))
    )

    (:action move-East
        :parameters (?p - pacman ?l1 - loc ?l2 - loc)
        :precondition (and (pacman-at ?p ?l1) (east ?l2 ?l1) (not (= ?l1 ?l2)))
        :effect (and (not (pacman-at ?p ?l1)) (pacman-at ?p ?l2))
    )

    (:action move-North
        :parameters (?p - pacman ?l1 - loc ?l2 - loc)
        :precondition (and (pacman-at ?p ?l1) (north ?l2 ?l1) (not (= ?l1 ?l2)))
        :effect (and (not (pacman-at ?p ?l1)) (pacman-at ?p ?l2))
    )

     (:action eat-at
     	:parameters (?p - pacman ?l - loc)
     	:precondition (and (pacman-at ?p ?l) (dot-at ?l))
     	:effect (and (not (dot-at ?l)) (eaten ?l))
    )

    (:action move-South
        :parameters (?p - pacman ?l1 - loc ?l2 - loc)
        :precondition (and (pacman-at ?p ?l1) (south ?l2 ?l1) (not (= ?l1 ?l2)))
        :effect (and (not (pacman-at ?p ?l1)) (pacman-at ?p ?l2))
	)

)
