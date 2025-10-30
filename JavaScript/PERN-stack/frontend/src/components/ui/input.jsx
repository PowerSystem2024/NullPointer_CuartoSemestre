import { forwardRef } from "react"

const Input = forwardRef((props, ref) => {
  return (
    <input 
      className="bg-zinc-800 px-3 py-2 block my-2 w-full rounded text-white" 
      {...props} 
      ref={ref}
    />
  )
})

export default Input