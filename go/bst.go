package main

import "fmt"

type node struct {
	name   string
	key    int
	l_node *node
	r_node *node
}

type tree struct {
	root *node
	curr *node
}

func (t tree) insert(n *node) tree {
	if t.curr.key == n.key {
		fmt.Println("같은 노드입니다.")
	} else if t.curr.key < n.key {
		if t.curr.r_node == nil {
			t.curr.r_node = n
			t.curr = t.root
			return t
		} else {
			t.curr = t.curr.r_node
			t.insert(n)
		}
	} else {
		if t.curr.l_node == nil {
			t.curr.l_node = n
			t.curr = t.root
			return t
		} else {
			t.curr = t.curr.l_node
			t.insert(n)
		}
	}
	t.curr = t.root
	return t
}

func main() {

	// create tree & root_node
	root := node{"jeong", 100, nil, nil}
	t := tree{&root, &root}
	fmt.Println(t.root)

	// insert
	node1 := node{"park", 50, nil, nil}
	t = t.insert(&node1)
	fmt.Println(t.root.l_node)

	node2 := node{"jin", 10, nil, nil}
	t = t.insert(&node2)
	fmt.Println(t.root.l_node.l_node)

	node3 := node{"kong", 52, nil, nil}
	t = t.insert(&node3)
	fmt.Println(t.root.l_node.r_node)

	node4 := node{"kong", 1000, nil, nil}
	t = t.insert(&node4)
	fmt.Println(t.root.r_node)

}
