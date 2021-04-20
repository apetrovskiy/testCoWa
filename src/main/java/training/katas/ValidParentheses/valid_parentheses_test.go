package kata // _test

import (
	// . "codewarrior/kata"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Example Tests", func() {
	It("passes example tests", func() {
		Expect(ValidParentheses("()")).To(Equal(true))
		Expect(ValidParentheses(")")).To(Equal(false))
	})
})
